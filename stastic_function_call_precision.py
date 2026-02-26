import json
import re
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import os

# ======================
# 统计函数调用次数
# ======================
def count_function_calls(code: str) -> int:
    def_pattern = r'^\s*def\s+(\w+)\s*\('
    lines = code.split("\n")

    function_names = set()
    for line in lines:
        m = re.match(def_pattern, line)
        if m:
            function_names.add(m.group(1))

    call_count = 0
    for line in lines:
        for name in function_names:
            if f"{name}(" in line and not re.match(rf'^\s*def\s+{name}', line):
                call_count += line.count(f"{name}(")

    return call_count


# Bucketing for plotting: [1, 2-3, 4-6, 7-10, 10+]
BUCKET_LABELS = ["1", "2-3", "4-6", "7-10", "10+"]

def map_count_to_bucket(count: int):
    if count <= 0:
        return None
    if count == 1:
        return "1"
    if 2 <= count <= 3:
        return "2-3"
    if 4 <= count <= 6:
        return "4-6"
    if 7 <= count <= 10:
        return "7-10"
    # count >= 11
    return "10+"


# ======================
# 单模型分析（保留原功能）
# ======================
def analyze_accuracy_vs_function_calls(
    dataset_file: str,
    result_file: str,
    return_stats: bool = False,
):
    code_map = {}
    with open(dataset_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                code_map[obj["id"]] = obj.get("task", {}).get("code", "")

    result_map = {}
    with open(result_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                result_map[obj["id"]] = bool(obj.get("correct", False))

    stats = defaultdict(lambda: {"correct": 0, "total": 0})
    missing = 0

    for id_, code in code_map.items():
        if id_ not in result_map:
            missing += 1
            continue

        call_count = count_function_calls(code)
        bucket = map_count_to_bucket(call_count)
        if bucket is None:
            # skip samples with zero function calls for this bucketed plot
            continue

        is_correct = result_map[id_]

        stats[bucket]["total"] += 1
        if is_correct:
            stats[bucket]["correct"] += 1

    # Use the fixed bucket order for plotting
    call_counts = [b for b in BUCKET_LABELS if b in stats]
    accuracies = [stats[c]["correct"] / stats[c]["total"] for c in call_counts]

    # ===== 单模型画图 =====
    result_name = os.path.basename(result_file).replace(".jsonl", "")
    plt.figure(figsize=(7, 5))
    plt.plot(call_counts, accuracies, marker="o", linewidth=2)

    plt.xlabel("Function Call Bucket")
    plt.ylabel("Accuracy")
    plt.title(f"Accuracy vs. Function Call Bucket ({result_name})")

    plt.ylim(0, 1.05)
    plt.grid(True, linestyle="--", alpha=0.5)

    # Plot on integer x positions and label ticks with bucket labels
    x = list(range(len(call_counts)))
    plt.clf()
    plt.figure(figsize=(7, 5))
    plt.plot(x, accuracies, marker="o", linewidth=2)
    plt.xlabel("Function Call Bucket")
    plt.ylabel("Accuracy")
    plt.title(f"Accuracy vs. Function Call Bucket ({result_name})")
    plt.ylim(0, 1.05)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(x, call_counts)
    for xi, yi in zip(x, accuracies):
        plt.text(xi, yi + 0.03, f"{yi:.2f}", ha="center", fontsize=9)

    os.makedirs("./pictures", exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"./pictures/accuracy_vs_function_calls_{result_name}.png", dpi=300)
    plt.close()

    print(f"✓ Saved figure: accuracy_vs_function_calls_{result_name}.png")
    print(f"✓ Matched samples: {sum(v['total'] for v in stats.values())}")
    print(f"⚠ Missing results: {missing}")

    if return_stats:
        return stats


# ======================
# 多模型平均分析（新增）
# ======================
def analyze_average_accuracy_vs_function_calls(
    dataset_file: str,
    result_files: list,
):
    all_model_stats = []

    for rf in result_files:
        stats = analyze_accuracy_vs_function_calls(
            dataset_file,
            rf,
            return_stats=True
        )
        all_model_stats.append(stats)

    # Use fixed bucket order and compute average accuracy per bucket
    all_call_counts = [b for b in BUCKET_LABELS if any((b in stats and stats[b]["total"] > 0) for stats in all_model_stats)]

    avg_accuracies = []
    for c in all_call_counts:
        accs = []
        for stats in all_model_stats:
            if c in stats and stats[c]["total"] > 0:
                accs.append(stats[c]["correct"] / stats[c]["total"])
        avg_accuracies.append(np.mean(accs) if accs else 0.0)

    # ===== 平均准确率画图 =====
    # Plot using integer x positions and label ticks with bucket labels
    x = list(range(len(all_call_counts)))
    plt.figure(figsize=(7, 5))
    plt.plot(x, avg_accuracies, marker="o", linewidth=2, color="black")

    plt.xlabel("Function Call Bucket")
    plt.ylabel("Average Accuracy")
    plt.title("Average Accuracy vs. Function Call Bucket (All Models)")

    plt.ylim(0, 1.05)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(x, all_call_counts)

    for xi, yi in zip(x, avg_accuracies):
        plt.text(xi, yi + 0.03, f"{yi:.2f}", ha="center", fontsize=9)

    os.makedirs("./pictures", exist_ok=True)
    plt.tight_layout()
    plt.savefig("./pictures/accuracy_vs_function_calls_average.png", dpi=300)
    plt.close()

    print("✓ Saved figure: accuracy_vs_function_calls_average.png")


# ======================
# 入口
# ======================
if __name__ == "__main__":
    dataset_file = "./data/Qwen3-32B_vs_Qwen3-14B_size500.jsonl"
    result_files = [
        "./result/Qwen3-32B_thought.jsonl",
        "./result/Qwen3-14B_thought.jsonl",
        "./result/Qwen3-8B_thought.jsonl",
        "./result/Qwen3-Coder-30B-A3B-Instruct_thought.jsonl",
        "./result/deepseek-coder-33b-instruct_thought.jsonl",
        "./result/QwQ-32B_thought.jsonl"
    ]

    # 分别统计（原行为）
    for rf in result_files:
        analyze_accuracy_vs_function_calls(dataset_file, rf)

    # ===== 是否统计平均 =====
    AVERAGE = True
    if AVERAGE:
        analyze_average_accuracy_vs_function_calls(
            dataset_file,
            result_files
        )
