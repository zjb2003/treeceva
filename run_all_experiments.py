#!/usr/bin/env python3
"""
run_all_experiments.py
FuncCodeBench 主评估实验 — 并行运行所有 API 模型（cot / ncot 双路）

用法:
    python run_all_experiments.py                                      # 全部模型 × both（默认 8 并发）
    python run_all_experiments.py --mode cot                           # 只跑 cot
    python run_all_experiments.py --mode ncot                          # 只跑 ncot
    python run_all_experiments.py --workers 12                         # 指定并发数
    python run_all_experiments.py --dry-run                            # 仅打印命令，不执行
    python run_all_experiments.py --skip-done                          # 跳过已有完整结果的 case
    python run_all_experiments.py --only gpt-4o,gpt-5,grok-2          # 只运行指定模型（逗号分隔）

跑 6 个模型的 12 个 case:
    python run_all_experiments.py \
        --only gpt-4o,gpt-4.1-mini,o1,gpt-5,grok-2,grok-3-mini-beta \
        --workers 12
"""

import argparse
import logging
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# ==============================================================
# 日志配置
# ==============================================================
_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(f"run_all_{_ts}.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)
_print_lock = threading.Lock()

# ==============================================================
# 路径
# cot  结果 → result-cot/
# ncot 结果 → result-ncot/
# ==============================================================
SCRIPT_DIR      = Path(__file__).parent
INPUT_FILE      = SCRIPT_DIR / "data" / "cross_function_with_assert.jsonl"
RESULT_COT_DIR  = SCRIPT_DIR / "result-cot"
RESULT_NCOT_DIR = SCRIPT_DIR / "result-ncot"

for _d in (RESULT_COT_DIR, RESULT_NCOT_DIR):
    _d.mkdir(exist_ok=True)

# ==============================================================
# API 密钥 & Endpoint
# ==============================================================
PARATERA_KEY    = "sk-0ABx5wpLhRLL-ZKEwiKY_w"
PARATERA_URL    = "https://llmapi.paratera.com/v1/"

EZAI_URL        = "https://api.ezai88.com/v1"
EZAI_GPT_KEY    = "sk-NdltMkcERI1Klsyjo4Trzo1sKph6blaaFo0vulEjizV4g8ts"
EZAI_GEMINI_KEY = "sk-C28dDH1FD2RPrzNzhSVd1brwUJNWgdcCcccEJZglCdWob2kj"
EZAI_CLAUDE_KEY = "sk-gq8qRNNiNIjS0x8tzfMl8F9bscL4wopT7oA2qD2FU8xKTrnp"

# ==============================================================
# 推理通用参数
# ==============================================================
TEMPERATURE    = 0
MAX_NEW_TOKENS = 2048
BATCH_SIZE     = 4

# ==============================================================
# 模型列表
# 注意：不再含 "cot" 字段，由 build_tasks() 自动展开为 cot / ncot 两个 task
# ==============================================================
MODELS = [
    # ──────────────────── Paratera: Qwen3 系列 ────────────────────
    {
        "api_model": "Qwen3-Next-80B-A3B-Instruct",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": "Qwen3-Next-80B-Instruct",
    },
    {
        "api_model": "Qwen3-235B-A22B-Instruct-2507",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": "Qwen3-235B-Instruct",
    },
    {
        "api_model": "Qwen3-32B",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "Qwen2.5-72B-Instruct",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: DeepSeek 系列 ─────────────────
    {
        "api_model": "DeepSeek-V3.2",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "DeepSeek-V3.2-Thinking",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": True, "output_name": None,
    },
    {
        "api_model": "DeepSeek-V3.1",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "DeepSeek-R1",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": True, "output_name": None,
    },

    # ──────────────────── Paratera: Kimi ──────────────────────────
    {
        "api_model": "Kimi-K2",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: GLM 系列 ──────────────────────
    {
        "api_model": "GLM-4.6",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "GLM-4.5",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "GLM-5",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "GLM-4-Flash",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: MiniMax 系列 ──────────────────
    {
        "api_model": "MiniMax-M1-80k",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "MiniMax-M2",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "MiniMax-M2.5",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: Coder 系列 ────────────────────
    {
        "api_model": "Qwen3-Coder-480B-A35B-Instruct",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: GPT 系列 ──────────────────────────
    {
        "api_model": "gpt-3.5-turbo",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-4",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-4o",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-4.1-mini",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "o1",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-5",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: Grok 系列 ─────────────────────────
    {
        "api_model": "grok-2",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "grok-3-mini-beta",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "grok-4",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: Gemini 系列 ───────────────────────
    {
        "api_model": "gemini-2.0-flash",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gemini-2.5-flash",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gemini-2.5-pro",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gemini-3-flash-preview",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: Claude 系列 ───────────────────────
    {
        "api_model": "claude-3-7-sonnet-20250219",
        "base_url": EZAI_URL, "api_key": EZAI_CLAUDE_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "claude-sonnet-4-20250514",
        "base_url": EZAI_URL, "api_key": EZAI_CLAUDE_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "claude-sonnet-4-5-20250929",
        "base_url": EZAI_URL, "api_key": EZAI_CLAUDE_KEY,
        "enable_thinking": False, "output_name": None,
    },
]


# ==============================================================
# 工具函数
# ==============================================================

def count_jsonl_lines(path: Path) -> int:
    if not path.exists():
        return 0
    count = 0
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                count += 1
    return count


def result_dir(cot: bool) -> Path:
    """根据 cot 标志返回对应的结果目录。"""
    return RESULT_COT_DIR if cot else RESULT_NCOT_DIR


def get_output_path(task: dict) -> Path:
    name = task.get("output_name") or task["api_model"]
    return result_dir(task["cot"]) / f"{name}.jsonl"


def get_log_path(task: dict) -> Path:
    name = task.get("output_name") or task["api_model"]
    return result_dir(task["cot"]) / f"{name}_analysis.log"


def get_proc_log_path(task: dict) -> Path:
    name = task.get("output_name") or task["api_model"]
    return result_dir(task["cot"]) / f"{name}_proc.log"


def task_label(task: dict) -> str:
    """用于日志的任务标签，含 [cot] / [ncot] 后缀。"""
    name = task.get("output_name") or task["api_model"]
    return f"{name}[{'cot' if task['cot'] else 'ncot'}]"


def build_tasks(models: list[dict], mode: str) -> list[dict]:
    """
    将模型列表按 mode 展开为 task 列表。
      both → 每个模型生成 ncot + cot 两个 task
      cot  → 只生成 cot task
      ncot → 只生成 ncot task
    """
    cot_flags: list[bool] = {
        "both": [False, True],
        "cot":  [True],
        "ncot": [False],
    }[mode]

    tasks = []
    for cfg in models:
        for cot in cot_flags:
            task = {k: v for k, v in cfg.items() if k != "cot"}  # 丢弃旧 cot 字段（如有）
            task["cot"] = cot
            tasks.append(task)
    return tasks


# ==============================================================
# 单任务运行逻辑（在线程池中被调用）
# ==============================================================

def run_task(task: dict, dry_run: bool = False) -> tuple[str, bool]:
    """
    运行单个 task 的 eval_runner + analyze_results。
    返回 (task_label, success)。
    此函数在子线程中执行，所有输出写文件，不直接打印到终端。
    """
    label       = task_label(task)
    output_file = get_output_path(task)
    log_file    = get_log_path(task)
    proc_log    = get_proc_log_path(task)

    with _print_lock:
        logger.info("▶ START [%s]  →  %s", label, output_file)

    # ── Step 1: eval_runner ──────────────────────────────────────
    eval_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "eval_runner.py"),
        "--backend",        "api",
        "--input",          str(INPUT_FILE),
        "--output",         str(output_file),
        "--api_base_url",   task["base_url"],
        "--api_model",      task["api_model"],
        "--api_key",        task["api_key"],
        "--temperature",    str(TEMPERATURE),
        "--max_new_tokens", str(MAX_NEW_TOKENS),
        "--batch_size",     str(BATCH_SIZE),
        "--resume",
    ]
    if task.get("enable_thinking"):
        eval_cmd.append("--enable_thinking")
    if task["cot"]:
        eval_cmd.append("--cot")

    with _print_lock:
        logger.info("CMD [%s]: %s", label, " ".join(eval_cmd))

    if not dry_run:
        with proc_log.open("w", encoding="utf-8") as pf:
            ret = subprocess.run(eval_cmd, cwd=str(SCRIPT_DIR), stdout=pf, stderr=pf)

        if ret.returncode != 0:
            with _print_lock:
                logger.error(
                    "❌ FAILED [%s]  code=%d  详情见: %s",
                    label, ret.returncode, proc_log,
                )
            return label, False

    # ── Step 2: analyze_results ──────────────────────────────────
    analyze_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "analyze_results.py"),
        str(output_file),
    ]

    if not dry_run:
        with log_file.open("w", encoding="utf-8") as lf:
            subprocess.run(analyze_cmd, stdout=lf, stderr=lf, cwd=str(SCRIPT_DIR))

    with _print_lock:
        logger.info("✅ DONE  [%s]", label)

    return label, True


# ==============================================================
# 主流程
# ==============================================================

def main():
    ap = argparse.ArgumentParser(
        description="FuncCodeBench 主评估实验并行运行器（cot/ncot 双路）"
    )
    ap.add_argument(
        "--mode", choices=["both", "cot", "ncot"], default="both",
        help="运行模式：both=cot+ncot（默认），cot=仅cot，ncot=仅ncot",
    )
    ap.add_argument(
        "--workers", type=int, default=8,
        help="最大并发 task 数（默认 8）",
    )
    ap.add_argument("--dry-run",   action="store_true", help="只打印命令，不实际执行")
    ap.add_argument("--skip-done", action="store_true", help="结果文件行数 ≥ 数据集行数时自动跳过")
    ap.add_argument(
        "--only", type=str, default=None,
        help="逗号分隔的模型名（api_model 或 output_name），只运行这些模型",
    )
    args = ap.parse_args()

    total_samples = count_jsonl_lines(INPUT_FILE)
    logger.info("数据集: %s  |  总样本数: %d", INPUT_FILE, total_samples)
    logger.info("结果目录: result-cot/  &  result-ncot/")
    logger.info("运行模式: %s  |  并发数: %d", args.mode, args.workers)

    # ── 模型过滤（--only） ─────────────────────────────────────────
    models = MODELS
    if args.only:
        only_set = set(args.only.split(","))
        models = [
            m for m in MODELS
            if m["api_model"] in only_set
            or (m.get("output_name") or "") in only_set
        ]
        logger.info("按 --only 筛选后，共 %d 个模型", len(models))

    # ── 展开为 tasks ──────────────────────────────────────────────
    all_tasks = build_tasks(models, args.mode)
    logger.info("总 task 数: %d", len(all_tasks))

    # ── skip-done 预筛选 ──────────────────────────────────────────
    to_run:       list[dict] = []
    skipped_list: list[str]  = []

    for task in all_tasks:
        label        = task_label(task)
        output_file  = get_output_path(task)
        existing_cnt = count_jsonl_lines(output_file)

        logger.info("%-55s | 已有 %d / %d 条", label, existing_cnt, total_samples)

        if args.skip_done and existing_cnt >= total_samples:
            logger.info("⏭  已完整，跳过: %s", label)
            skipped_list.append(label)
        else:
            to_run.append(task)

    logger.info("=" * 60)
    logger.info("待运行 tasks: %d  |  并发数: %d", len(to_run), args.workers)
    logger.info("=" * 60)

    success_list: list[str] = []
    failed_list:  list[str] = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(run_task, task, args.dry_run): task
            for task in to_run
        }

        for future in as_completed(futures):
            task = futures[future]
            try:
                label, ok = future.result()
            except Exception as exc:
                label = task_label(task)
                logger.exception("💥 未捕获异常 [%s]: %s", label, exc)
                ok = False

            (success_list if ok else failed_list).append(label)

    # ── 汇总 ──────────────────────────────────────────────────────
    logger.info("=" * 60)
    logger.info(
        "汇总  总 task=%d  成功=%d  跳过=%d  失败=%d",
        len(all_tasks), len(success_list), len(skipped_list), len(failed_list),
    )
    if success_list:
        logger.info("✅ 成功: %s", ", ".join(sorted(success_list)))
    if skipped_list:
        logger.info("⏭  跳过: %s", ", ".join(skipped_list))
    if failed_list:
        logger.error("❌ 失败: %s", ", ".join(sorted(failed_list)))
        logger.error("失败 task 的详细日志在对应 result-*/..._proc.log 中")


if __name__ == "__main__":
    main()