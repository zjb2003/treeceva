#!/usr/bin/env python3
"""
retry_invalid.py

对 result-cot/ 和 result-ncot/ 中的结果文件做两件事：
  1. 如果文件不存在 → 先调用 eval_runner.py 完整跑一遍（补全）
  2. 如果文件存在   → 扫描 error 为 no_assert_found / empty_output 的条目，
                      直接调用 API 重试（每条最多 MAX_RETRIES 次）

10 个模型 × cot/ncot = 20 个 task，完全并行。
终端以两级进度条实时展示进展；详细日志写入文件。

用法:
    python retry_invalid.py
    python retry_invalid.py --dry-run
    python retry_invalid.py --workers 10
    python retry_invalid.py --only grok-4,gemini-2.0-flash
    python retry_invalid.py --mode cot
"""

import argparse
import json
import logging
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from openai import OpenAI
from tqdm import tqdm

from dataset import iter_jsonl, extract_original_assert, parse_assert_answer
from prompt import build_user_prompt

# ══════════════════════════════════════════════════════════════
# 日志配置
#   INFO+    → 文件（完整记录）
#   WARNING+ → 终端（通过 tqdm.write，避免打断进度条）
# ══════════════════════════════════════════════════════════════
_ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
_LOG_FILE = f"retry_invalid_{_ts}.log"
_LOG_FMT  = "%(asctime)s | %(levelname)s | %(message)s"


class _TqdmHandler(logging.Handler):
    """将日志通过 tqdm.write() 输出，防止进度条被日志行打断。"""
    def emit(self, record: logging.LogRecord) -> None:
        try:
            tqdm.write(self.format(record), file=sys.stdout)
        except Exception:
            self.handleError(record)


_file_hdlr = logging.FileHandler(_LOG_FILE, encoding="utf-8")
_file_hdlr.setLevel(logging.INFO)
_file_hdlr.setFormatter(logging.Formatter(_LOG_FMT))

_term_hdlr = _TqdmHandler()
_term_hdlr.setLevel(logging.WARNING)   # 终端只显示 WARNING / ERROR / CRITICAL
_term_hdlr.setFormatter(logging.Formatter(_LOG_FMT))

_root = logging.getLogger()
_root.setLevel(logging.INFO)
_root.handlers.clear()
_root.addHandler(_file_hdlr)
_root.addHandler(_term_hdlr)

logger = logging.getLogger(__name__)

# ══════════════════════════════════════════════════════════════
# 路径 & API 配置
# ══════════════════════════════════════════════════════════════
SCRIPT_DIR      = Path(__file__).parent
INPUT_FILE      = SCRIPT_DIR / "data" / "cross_function_with_assert.jsonl"
RESULT_COT_DIR  = SCRIPT_DIR / "result-cot"
RESULT_NCOT_DIR = SCRIPT_DIR / "result-ncot"

for _d in (RESULT_COT_DIR, RESULT_NCOT_DIR):
    _d.mkdir(exist_ok=True)

PARATERA_KEY    = "sk-0ABx5wpLhRLL-ZKEwiKY_w"
PARATERA_URL    = "https://llmapi.paratera.com/v1/"
EZAI_URL        = "https://api.ezai88.com/v1"
EZAI_GPT_KEY    = "sk-NdltMkcERI1Klsyjo4Trzo1sKph6blaaFo0vulEjizV4g8ts"
EZAI_GEMINI_KEY = "sk-C28dDH1FD2RPrzNzhSVd1brwUJNWgdcCcccEJZglCdWob2kj"

RETRY_MODELS: list[dict] = [
    {"api_model": "DeepSeek-V3.2-Thinking", "base_url": PARATERA_URL, "api_key": PARATERA_KEY, "enable_thinking": True,  "output_name": None},
    {"api_model": "GLM-4.5",                "base_url": PARATERA_URL, "api_key": PARATERA_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "GLM-5",                  "base_url": PARATERA_URL, "api_key": PARATERA_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "MiniMax-M1-80k",         "base_url": PARATERA_URL, "api_key": PARATERA_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "MiniMax-M2",             "base_url": PARATERA_URL, "api_key": PARATERA_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "MiniMax-M2.5",           "base_url": PARATERA_URL, "api_key": PARATERA_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "gemini-2.0-flash",       "base_url": EZAI_URL,     "api_key": EZAI_GEMINI_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "gemini-2.5-flash",       "base_url": EZAI_URL,     "api_key": EZAI_GEMINI_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "gemini-3-flash-preview", "base_url": EZAI_URL,     "api_key": EZAI_GEMINI_KEY, "enable_thinking": False, "output_name": None},
    {"api_model": "grok-4",                 "base_url": EZAI_URL,     "api_key": EZAI_GPT_KEY,    "enable_thinking": False, "output_name": None},
]

TEMPERATURE    = 0
MAX_NEW_TOKENS = 2048
MAX_RETRIES    = 3
BATCH_SIZE     = 4
RETRY_ERRORS   = {"no_assert_found", "empty_output"}


# ══════════════════════════════════════════════════════════════
# 进度管理器（线程安全）
# ══════════════════════════════════════════════════════════════

class ProgressManager:
    """
    双层进度条（线程安全）：

      Tasks（上）: 20 个 task 的完成状态
                  ✓完成  ✗失败  ⏳运行中
      Items（下）: 所有待重试条目的处理进度
                  ✓改善  ✗未改善
    """

    def __init__(self, total_tasks: int, total_items: int) -> None:
        self._lock = threading.Lock()

        self._task_bar = tqdm(
            total=total_tasks,
            desc="Tasks",
            position=0,
            leave=True,
            ncols=90,
        )
        # total_items 为 0 说明预扫描阶段所有文件均缺失，用 None 表示未知总量
        self._item_bar = tqdm(
            total=total_items if total_items > 0 else None,
            desc="Items",
            position=1,
            leave=True,
            ncols=90,
        )
        self._ok  = 0   # 任务：成功完成
        self._nok = 0   # 任务：异常/失败
        self._run = 0   # 任务：正在运行
        self._imp = 0   # 条目：已改善
        self._unc = 0   # 条目：未改善

        self._flush_task()
        self._flush_item()

    # ── task 生命周期 ─────────────────────────────────────────

    def task_start(self) -> None:
        with self._lock:
            self._run += 1
            self._flush_task()

    def task_done(self, ok: bool) -> None:
        with self._lock:
            self._run = max(0, self._run - 1)
            if ok:
                self._ok += 1
            else:
                self._nok += 1
            self._task_bar.update(1)
            self._flush_task()

    # ── item 生命周期 ─────────────────────────────────────────

    def add_items(self, n: int) -> None:
        """eval_runner 新建文件后，动态追加条目数到 item_bar 总量。"""
        with self._lock:
            cur = self._item_bar.total or 0
            self._item_bar.total = cur + n
            self._item_bar.refresh()

    def item_done(self, improved: bool) -> None:
        with self._lock:
            if improved:
                self._imp += 1
            else:
                self._unc += 1
            self._item_bar.update(1)
            self._flush_item()

    # ── 内部刷新（须在 _lock 内调用）────────────────────────

    def _flush_task(self) -> None:
        self._task_bar.set_postfix(
            {"✓完成": self._ok, "✗失败": self._nok, "⏳运行": self._run},
            refresh=True,
        )

    def _flush_item(self) -> None:
        self._item_bar.set_postfix(
            {"✓改善": self._imp, "✗未改善": self._unc},
            refresh=True,
        )

    def close(self) -> None:
        self._task_bar.close()
        self._item_bar.close()


# ══════════════════════════════════════════════════════════════
# 工具函数
# ══════════════════════════════════════════════════════════════

def _model_name(cfg: dict) -> str:
    return cfg.get("output_name") or cfg["api_model"]


def _output_path(cfg: dict, cot: bool) -> Path:
    d = RESULT_COT_DIR if cot else RESULT_NCOT_DIR
    return d / f"{_model_name(cfg)}_thought.jsonl"


def _task_label(cfg: dict, cot: bool) -> str:
    return f"{_model_name(cfg)}[{'cot' if cot else 'ncot'}]"


def load_dataset(path: Path) -> dict:
    return {s["id"]: s for s in iter_jsonl(path)}


def prescan_retry_count(models: list[dict], cot_flags: list[bool]) -> int:
    """预扫描已存在的结果文件，统计需要重试的条目总数（用于初始化 item_bar）。"""
    total = 0
    for cfg in models:
        for cot in cot_flags:
            opath = _output_path(cfg, cot)
            if opath.exists():
                for r in iter_jsonl(opath):
                    if r.get("error") in RETRY_ERRORS:
                        total += 1
    return total


# ══════════════════════════════════════════════════════════════
# API 调用
# ══════════════════════════════════════════════════════════════

def call_api_once(
    client:          OpenAI,
    model:           str,
    prompt:          str,
    enable_thinking: bool,
) -> str:
    """
    发起单次 API 请求，返回模型输出文本。失败时返回空字符串。

    Bug 修复：
      1. content 可能为 None（部分模型在思考模式下返回空 content），
         直接 .strip() 会抛出 AttributeError，需先判空。
      2. 发送 {"role": "system", "content": ""} 会导致 Gemini 返回 400
         (system_instruction.parts[0].data required oneof field)。
         由于 build_user_prompt 已将 system 指令拼入 prompt，
         此处只需发送单条 user 消息即可。
    """
    try:
        kwargs: dict = {
            "model":       model,
            "messages":    [{"role": "user", "content": prompt}],   # ← 修复 Bug 2：不发送空 system 消息
            "max_tokens":  MAX_NEW_TOKENS,
            "temperature": TEMPERATURE,
            "stream":      False,
        }
        if enable_thinking:
            kwargs["extra_body"] = {"enable_thinking": True}

        resp    = client.chat.completions.create(**kwargs)
        content = resp.choices[0].message.content
        return content.strip() if content is not None else ""       # ← 修复 Bug 1：避免 None.strip()
    except Exception as exc:
        logger.warning("API call failed: %s", exc)
        return ""


def retry_entry(
    entry:           dict,
    sample:          dict,
    client:          OpenAI,
    model:           str,
    enable_thinking: bool,
    cot:             bool,
) -> tuple[dict, bool, int]:
    """对单条 entry 最多重试 MAX_RETRIES 次。返回 (updated_entry, improved, attempts)。"""
    code        = sample["task"]["code"]
    gold        = sample["task"].get("answer")
    orig_assert = extract_original_assert(code)
    prompt      = build_user_prompt(code, cot=cot)

    # 代码中根本没有带 ?? 的 assert 行，无法解析，不重试
    if orig_assert is None:
        return entry, False, 0

    last_nonempty_raw: str = entry.get("raw_output") or ""

    for attempt in range(1, MAX_RETRIES + 1):
        raw = call_api_once(client, model, prompt, enable_thinking)
        if raw:
            last_nonempty_raw = raw

        pred, err = parse_assert_answer(raw, orig_assert)
        if pred is not None:
            ok = gold is not None and abs(float(pred) - float(gold)) <= 1e-6
            entry.update(
                predicted_answer=pred, gold_answer=gold,
                correct=ok, error=err, raw_output=raw,
            )
            return entry, True, attempt

    # 全部失败：若有更新的非空输出，也写回（便于后续 analyze_results 重新解析）
    if last_nonempty_raw != (entry.get("raw_output") or ""):
        entry["raw_output"] = last_nonempty_raw
    return entry, False, MAX_RETRIES


def run_eval_runner(cfg: dict, cot: bool, output_path: Path) -> bool:
    """文件不存在时，调用 eval_runner.py 完整运行。返回是否成功。"""
    label    = _task_label(cfg, cot)
    proc_log = output_path.parent / (output_path.stem + "_eval_proc.log")

    cmd = [
        sys.executable, str(SCRIPT_DIR / "eval_runner.py"),
        "--backend",      "api",
        "--input",        str(INPUT_FILE),
        "--output",       str(output_path),
        "--api_base_url", cfg["base_url"],
        "--api_model",    cfg["api_model"],
        "--api_key",      cfg["api_key"],
        "--temperature",  str(TEMPERATURE),
        "--max_new_tokens", str(MAX_NEW_TOKENS),
        "--batch_size",   str(BATCH_SIZE),
        "--resume",
    ]
    if cfg.get("enable_thinking"):
        cmd.append("--enable_thinking")
    if cot:
        cmd.append("--cot")

    logger.info("[%s] eval_runner CMD: %s", label, " ".join(cmd))
    with proc_log.open("w", encoding="utf-8") as pf:
        ret = subprocess.run(cmd, cwd=str(SCRIPT_DIR), stdout=pf, stderr=pf)

    if ret.returncode != 0:
        logger.error("[%s] eval_runner 失败 code=%d 详见 %s", label, ret.returncode, proc_log)
    return ret.returncode == 0


# ══════════════════════════════════════════════════════════════
# 单 task —— 线程入口
# ══════════════════════════════════════════════════════════════

def process_task(
    cfg:      dict,
    cot:      bool,
    dataset:  dict,
    dry_run:  bool,
    progress: ProgressManager,
) -> tuple[str, int, int]:
    """
    处理一个 (模型, cot) 组合。
    返回 (label, total_retried, total_improved)。

    使用 try/finally 确保 progress.task_done() 在所有退出路径上都被调用。
    """
    label      = _task_label(cfg, cot)
    opath      = _output_path(cfg, cot)
    task_ok    = False
    n_retried  = 0
    n_improved = 0

    logger.info("▶ START [%s]  →  %s", label, opath)
    progress.task_start()

    try:
        # ── Step 1: 文件不存在 → 先用 eval_runner 补全 ───────────
        file_existed = opath.exists()
        if not file_existed:
            logger.info("[%s] 文件缺失，执行 eval_runner.py", label)
            if dry_run:
                logger.info("[%s] --dry-run，跳过 eval_runner.py", label)
                task_ok = True
                return label, 0, 0
            if not run_eval_runner(cfg, cot, opath):
                return label, 0, 0   # task_ok 保持 False

        # ── Step 2: 扫描需要重试的条目 ───────────────────────────
        results: list[dict] = []
        with opath.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))

        retry_idx: list[int] = [
            i for i, r in enumerate(results)
            if r.get("error") in RETRY_ERRORS
        ]
        logger.info("[%s] 总 %d 条  |  需重试 %d 条", label, len(results), len(retry_idx))

        if not retry_idx:
            logger.info("✅ [%s] 无需重试", label)
            task_ok = True
            return label, 0, 0

        # 若文件是本次 eval_runner 新建的，prescan 未统计这批条目，需动态追加
        if not file_existed:
            progress.add_items(len(retry_idx))

        if dry_run:
            logger.info("[%s] --dry-run，跳过重试 API 调用", label)
            task_ok = True
            return label, len(retry_idx), 0

        # ── Step 3: 逐条重试 ─────────────────────────────────────
        client = OpenAI(base_url=cfg["base_url"], api_key=cfg["api_key"], timeout=300.0)

        for seq, i in enumerate(retry_idx, 1):
            entry = results[i]
            sid   = entry.get("id", "")

            if sid not in dataset:
                logger.warning("[%s] id=%s 不在数据集中，跳过", label, sid)
                progress.item_done(improved=False)
                n_retried += 1
                continue

            updated, improved, attempts = retry_entry(
                entry=entry,
                sample=dataset[sid],
                client=client,
                model=cfg["api_model"],
                enable_thinking=cfg.get("enable_thinking", False),
                cot=cot,
            )
            results[i] = updated
            n_retried  += 1
            if improved:
                n_improved += 1

            logger.info(
                "[%s] %s (%d/%d) id=%-22s  试=%d  pred=%s",
                label, "✓" if improved else "✗",
                seq, len(retry_idx), sid, attempts,
                updated.get("predicted_answer"),
            )
            progress.item_done(improved=improved)

        # ── Step 4: 原子写回（.tmp → rename，避免写到一半崩溃）──
        tmp = opath.parent / (opath.stem + ".tmp")
        with tmp.open("w", encoding="utf-8") as f:
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        tmp.replace(opath)

        logger.info("✅ DONE [%s]  重试=%d  改善=%d  已写回: %s",
                    label, n_retried, n_improved, opath)
        task_ok = True
        return label, n_retried, n_improved

    except Exception as exc:
        logger.exception("💥 [%s] 未捕获异常: %s", label, exc)
        return label, n_retried, n_improved

    finally:
        # 无论从哪条路径退出，都必须通知进度管理器此 task 已结束
        progress.task_done(ok=task_ok)


# ══════════════════════════════════════════════════════════════
# 主函数
# ══════════════════════════════════════════════════════════════

def main() -> None:
    ap = argparse.ArgumentParser(
        description="提升有效预测数：缺失文件自动补全，无效条目自动重试"
    )
    ap.add_argument("--workers", type=int, default=20,
                    help="并发线程数（默认 20，即全部 task 同时执行）")
    ap.add_argument("--dry-run", action="store_true",
                    help="只统计需要处理的条目数，不实际调用 API 或 eval_runner")
    ap.add_argument("--only", type=str, default=None,
                    help="逗号分隔的模型名（api_model 或 output_name），只处理这些模型")
    ap.add_argument("--mode", choices=["both", "cot", "ncot"], default="both",
                    help="只处理 cot / ncot / 两者（默认 both）")
    args = ap.parse_args()

    tqdm.write(f"=== retry_invalid.py 启动  |  详细日志 → {_LOG_FILE} ===")
    logger.info("=== retry_invalid.py 启动 ===")
    logger.info("mode=%s  workers=%d  dry_run=%s", args.mode, args.workers, args.dry_run)
    if args.dry_run:
        tqdm.write("⚠  --dry-run：只统计，不调用 API / eval_runner")

    if not INPUT_FILE.exists():
        logger.error("数据集文件不存在: %s", INPUT_FILE)
        sys.exit(1)

    tqdm.write(f"加载数据集 {INPUT_FILE.name} …")
    dataset = load_dataset(INPUT_FILE)
    tqdm.write(f"数据集加载完成，共 {len(dataset)} 条\n")

    # ── 模型过滤（--only）────────────────────────────────────
    models: list[dict] = RETRY_MODELS
    if args.only:
        only_set = {s.strip() for s in args.only.split(",")}
        models = [
            m for m in RETRY_MODELS
            if m["api_model"] in only_set or (m.get("output_name") or "") in only_set
        ]
        tqdm.write(f"--only 筛选后：{len(models)} 个模型")

    cot_flags: list[bool] = {"both": [False, True], "cot": [True], "ncot": [False]}[args.mode]
    all_tasks   = [(cfg, cot) for cfg in models for cot in cot_flags]
    total_tasks = len(all_tasks)

    # ── 预扫描：统计已有文件中待重试条目总数，供 item_bar 初始化 ──
    tqdm.write("预扫描已有结果文件 …")
    total_items = prescan_retry_count(models, cot_flags)
    tqdm.write(
        f"已知待重试条目: {total_items}"
        + ("  （eval_runner 补全后可能增加）" if total_items == 0 else "")
        + "\n"
    )

    # ── 初始化进度条 ──────────────────────────────────────────
    progress = ProgressManager(total_tasks=total_tasks, total_items=total_items)

    # ── 并行执行 ──────────────────────────────────────────────
    summary: list[tuple[str, int, int]] = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {
            pool.submit(process_task, cfg, cot, dataset, args.dry_run, progress): (cfg, cot)
            for cfg, cot in all_tasks
        }
        for fut in as_completed(future_map):
            cfg, cot = future_map[fut]
            try:
                summary.append(fut.result())
            except Exception as exc:
                lbl = _task_label(cfg, cot)
                logger.exception("💥 未捕获异常 [%s]: %s", lbl, exc)
                summary.append((lbl, 0, 0))

    progress.close()

    # ── 终端汇总表 ────────────────────────────────────────────
    tqdm.write("")
    tqdm.write("=" * 72)
    tqdm.write(f"{'Task':<50}  {'重试':>6}  {'改善':>6}")
    tqdm.write("-" * 72)
    total_r = total_i = 0
    for lbl, r, i in sorted(summary):
        tqdm.write(f"{lbl:<50}  {r:>6}  {i:>6}")
        total_r += r
        total_i += i
    tqdm.write("-" * 72)
    tqdm.write(f"{'合计':<50}  {total_r:>6}  {total_i:>6}")
    tqdm.write("=" * 72)
    tqdm.write(f"\n详细日志已写入: {_LOG_FILE}")

    # 完整汇总也写日志
    logger.info("=== 最终汇总 ===")
    for lbl, r, i in sorted(summary):
        logger.info("%-55s  retried=%d  improved=%d", lbl, r, i)
    logger.info("合计  retried=%d  improved=%d", total_r, total_i)


if __name__ == "__main__":
    main()