import json
import random
from pathlib import Path
from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt

# ======================
# 参数
# ======================
SIZES = [100, 500, 1000, 1500, 2000]
N_BOOTSTRAP = 100
SEED = 42

random.seed(SEED)
np.random.seed(SEED)

# ======================
# 工具函数
# ======================
def load_correct_map(path: Path) -> Dict[str, int]:
    """id -> correct(0/1)"""
    data = {}
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                data[obj["id"]] = int(obj["correct"])
    return data


def accuracy(correct_map: Dict[str, int], ids: List[str]) -> float:
    return sum(correct_map[i] for i in ids) / len(ids)


def load_original_dataset(path: Path) -> Dict[str, dict]:
    """id -> 原始数据条目"""
    data = {}
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                if "id" in obj:
                    data[obj["id"]] = obj
    return data


# ======================
# 绘图
# ======================
def plot_bootstrap_results(bootstrap_results, sizes):
    x = np.arange(len(sizes))
    model_pairs = [
        "Qwen3-32B vs Qwen3-14B",
        "Qwen3-14B vs Qwen3-8B",
    ]
    colors = ["tab:blue", "tab:orange"]
    offsets = [-0.15, 0.15]
    width = 0.25

    plt.figure(figsize=(8, 5))

    for pair, color, offset in zip(model_pairs, colors, offsets):
        data = [
            [r["diff"] for r in bootstrap_results[k][pair]]
            for k in sizes
        ]
        plt.boxplot(
            data,
            positions=x + offset,
            widths=width,
            patch_artist=True,
            showfliers=False,
            boxprops=dict(facecolor=color, alpha=0.7),
            medianprops=dict(color="black", linewidth=1.5),
        )

    plt.axhline(0, color="gray", linestyle="--")
    plt.xticks(x, sizes)
    plt.xlabel("data size")
    plt.ylabel("accuracy difference")
    plt.title("Bootstrap accuracy difference")
    plt.legend(
        handles=[
            plt.Line2D([0], [0], color="tab:blue", lw=6),
            plt.Line2D([0], [0], color="tab:orange", lw=6),
        ],
        labels=model_pairs,
        loc="upper left",
    )
    plt.tight_layout()
    plt.savefig("./pictures/bootstrap_diff.png", dpi=300)
    plt.close()


# ======================
# 核心：最终样本选择逻辑
# ======================
def extract_final_conservative_batch(bootstrap_results):
    """
    规则：
    1. 同一 k 下，32B-14B 和 14B-8B 的 IQR(25-75) 都 > 0
    2. 在该 k 下，选择 median 较小的模型对
    3. 选 diff 最接近 median 的 bootstrap 批次
    """
    for k in SIZES:
        pair_stats = {}

        for pair, records in bootstrap_results[k].items():
            diffs = [r["diff"] for r in records]
            pair_stats[pair] = {
                "p25": np.percentile(diffs, 25),
                "p75": np.percentile(diffs, 75),
                "median": np.median(diffs),
                "records": records,
            }

        # 条件 1：两个模型对 IQR 都 > 0
        if all(v["p25"] > 0 and v["p75"] > 0 for v in pair_stats.values()):
            # 条件 2：选 median 较小者
            selected_pair = min(
                pair_stats.items(),
                key=lambda x: x[1]["median"]
            )[0]

            stats = pair_stats[selected_pair]
            median = stats["median"]

            best = min(
                stats["records"],
                key=lambda r: abs(r["diff"] - median)
            )

            return {
                "sample_size": k,
                "model_pair": selected_pair,
                "median_diff": float(median),
                "p25": float(stats["p25"]),
                "p75": float(stats["p75"]),
                "selected_diff": float(best["diff"]),
                "sample_ids": best["sample_ids"],
            }

    raise RuntimeError("No dataset size satisfies dual IQR > 0 condition.")


def extract_original_samples(
    final_batch: dict,
    original_data: Dict[str, dict],
    output_dir: Path,
):
    output_dir.mkdir(parents=True, exist_ok=True)

    unique_ids = sorted(set(final_batch["sample_ids"]))
    extracted = [original_data[i] for i in unique_ids if i in original_data]

    pair = final_batch["model_pair"].replace(" ", "_")
    size = final_batch["sample_size"]

    out_path = output_dir / f"{pair}_size{size}.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for obj in extracted:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    print(f"[Saved] {out_path} | samples={len(extracted)}")


# ======================
# 主流程
# ======================
def main():
    base_dir = Path("./result")

    m8 = load_correct_map(base_dir / "Qwen3-8B_thought.jsonl")
    m14 = load_correct_map(base_dir / "Qwen3-14B_thought.jsonl")
    m32 = load_correct_map(base_dir / "Qwen3-32B_thought.jsonl")

    ids = sorted(m8.keys())
    assert ids == sorted(m14.keys()) == sorted(m32.keys())

    # bootstrap
    results = {}

    for k in SIZES:
        results[k] = {
            "Qwen3-32B vs Qwen3-14B": [],
            "Qwen3-14B vs Qwen3-8B": [],
        }

        for _ in range(N_BOOTSTRAP):
            sample_ids = random.sample(ids, k=k)

            acc_8 = accuracy(m8, sample_ids)
            acc_14 = accuracy(m14, sample_ids)
            acc_32 = accuracy(m32, sample_ids)

            results[k]["Qwen3-32B vs Qwen3-14B"].append({
                "diff": acc_32 - acc_14,
                "sample_ids": sample_ids,
            })
            results[k]["Qwen3-14B vs Qwen3-8B"].append({
                "diff": acc_14 - acc_8,
                "sample_ids": sample_ids,
            })

    # 画图
    plot_bootstrap_results(results, SIZES)

    # 选最终 batch
    final_batch = extract_final_conservative_batch(results)

    with open("final_selected_batch.json", "w", encoding="utf-8") as f:
        json.dump(final_batch, f, indent=2, ensure_ascii=False)

    print("\n=== Final selected batch ===")
    print(
        f"pair={final_batch['model_pair']} | "
        f"size={final_batch['sample_size']} | "
        f"median={final_batch['median_diff']:.4f} | "
        f"IQR=[{final_batch['p25']:.4f}, {final_batch['p75']:.4f}]"
    )

    # 从原始数据中抽取最终数据
    original_data = load_original_dataset(
        Path("./data/cross_function_2000_with_assert.jsonl")
    )

    extract_original_samples(
        final_batch=final_batch,
        original_data=original_data,
        output_dir=Path("./data"),
    )


if __name__ == "__main__":
    main()
