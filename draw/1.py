import matplotlib.pyplot as plt
import numpy as np

# ═══════════════════════════════════════════════════════════════
#   Main Evaluation Results  ─  Horizontal Bar Chart
#   Style: LiveCodeBench-inspired, academic publication quality
# ═══════════════════════════════════════════════════════════════

# ─── 1. 实验数据 ─────────────────────────────────────────────
# 格式: (模型名称,  准确率%,  类别)
# 类别: "closed" = 闭源API模型  |  "open" = 开源模型
data = [
    ("claude-sonnet-4-5-20250929",        76.0, "closed"),
    ("claude-sonnet-4-20250514",           67.8, "closed"),
    ("DeepSeek-V3.2-Thinking",             63.0, "closed"),
    ("grok-4",                             60.0, "closed"),
    ("DeepSeek-V3.2",                      55.4, "closed"),
    ("DeepSeek-V3.1",                      53.6, "closed"),
    ("gemini-3-flash-preview",             52.0, "closed"),
    ("Kimi-K2",                            50.8, "closed"),
    ("GLM-4.5",                            45.4, "closed"),
    ("gemini-2.5-flash",                   37.6, "closed"),
    ("MiniMax-M1-80k",                     35.0, "closed"),
    ("MiniMax-M2",                         26.0, "closed"),
    ("MiniMax-M2.5",                       26.0, "closed"),
    ("GLM-5",                              23.4, "closed"),
    ("gemini-2.0-flash",                   20.2, "closed"),
    ("claude-3-7-sonnet-20250219",         11.4, "closed"),
    ("Qwen3-235B-Instruct",                 8.6, "closed"),
    ("gpt-4",                               8.6, "closed"),
    ("Qwen3-Next-80B-Instruct",             8.2, "closed"),
    ("gpt-3.5-turbo",                       7.6, "closed"),
    ("gpt-4o",                              7.2, "closed"),
    ("Qwen2.5-72B-Instruct",                5.6, "closed"),
    ("gpt-4.1-mini",                        5.6, "closed"),
    ("Qwen3-Coder-480B-A35B-Instruct",      5.2, "closed"),
    ("GLM-4-Flash",                         4.6, "closed"),
    ("Qwen3-32B",                           4.4, "closed"),
    ("Qwen2.5-Coder-7B",                    4.2, "closed"),
    ("Qwen-2.5-Coder-7B-Instruct",          3.6, "closed"),
    # ─── 开源代码模型 ───────────────────────────
    ("deepseek-coder-33b-base",             3.6, "open"),
    ("CodeIO",                              3.4, "open"),
    ("starcoder2-15b",                      3.4, "open"),
    ("CodeLlama-34b-hf",                    3.4, "open"),
    ("CodeLlama-13b-hf",                    3.2, "open"),
    ("CodeReasoner-7b",                     2.8, "open"),
    ("deepseek-coder-6.7b-base",            2.6, "open"),
    ("codegemma-7b",                        2.6, "open"),
    ("gemma-7b",                            2.6, "open"),
    ("starcoder2-7b",                       2.2, "open"),
]

# ─── 2. 配色方案（对应参考图蓝/橙双色风格）──────────────────
C_BAR = "#5B9BD5"   # 闭源柱体颜色：蓝色
O_BAR = "#ED7D31"   # 开源柱体颜色：橙色
C_BG  = "#EBF3FB"   # 闭源区域背景：淡蓝
O_BG  = "#FDF0E6"   # 开源区域背景：淡橙
C_ANN = "#1F497D"   # 闭源标注文字：深蓝
O_ANN = "#7F3000"   # 开源标注文字：深橙

# ─── 3. 数据预处理 ───────────────────────────────────────────
models     = [d[0] for d in data]
accs       = [d[1] for d in data]
types      = [d[2] for d in data]
bar_colors = [C_BAR if t == "closed" else O_BAR for t in types]
n          = len(data)
n_closed   = sum(1 for t in types if t == "closed")   # 28
n_open     = n - n_closed                              # 10
y          = np.arange(n)

# ─── 4. 创建画布 ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 17))

# ─── 5. 背景区域着色 ──────────────────────────────────────────
ax.axhspan(-0.5,           n_closed - 0.5, color=C_BG, zorder=0)
ax.axhspan(n_closed - 0.5, n - 0.5,        color=O_BG, zorder=0)

# ─── 6. 绘制水平柱状图 ────────────────────────────────────────
bars = ax.barh(y, accs,
               color=bar_colors, height=0.70,
               edgecolor="none", zorder=2)

# ─── 7. 柱尾数值标签 ──────────────────────────────────────────
for bar, acc in zip(bars, accs):
    ax.text(
        bar.get_width() + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{acc:.1f}",
        va="center", ha="left",
        fontsize=20, color="#111111"
    )

# ─── 8. Y 轴（模型名称）──────────────────────────────────────
ax.set_yticks(y)
ax.set_yticklabels(models, fontsize=20, fontfamily="monospace")
ax.invert_yaxis()
ax.tick_params(axis="y", left=False, pad=5)

# ─── 9. X 轴 ─────────────────────────────────────────────────
ax.set_xlabel("Accuracy  (%)", fontsize=20, labelpad=6)
ax.set_xlim(0, 92)
ax.set_xticks(range(0, 81, 10))
ax.tick_params(axis="x", colors="#666666")
ax.xaxis.label.set_color("#444444")
ax.grid(False)

# ─── 10. 区域标注框 ───────────────────────────────────────────
mid_c = (n_closed - 1) / 2.0            # 闭源区域纵向中心 ≈ 13.5
mid_o = n_closed + (n_open - 1) / 2.0   # 开源区域纵向中心 ≈ 32.5

ann_kw = dict(boxstyle="round,pad=0.5", linewidth=0.9)
ax.text(78, mid_c,
        "Closed-Source\nAPI Models",
        ha="center", va="center", fontsize=20, color=C_ANN,
        bbox=dict(facecolor=C_BG, edgecolor=C_BAR, **ann_kw))
ax.text(78, mid_o,
        "Open-Source\nModels",
        ha="center", va="center", fontsize=20, color=O_ANN,
        bbox=dict(facecolor=O_BG, edgecolor=O_BAR, **ann_kw))

# ─── 11. 标题 ────────────────────────────────────────────────
ax.set_title("Main Evaluation Results",
             fontsize=30, fontweight="bold",
             fontfamily="serif", pad=12)

# ─── 12. 边框美化 ─────────────────────────────────────────────
for sp in ("top", "right", "left"):
    ax.spines[sp].set_visible(False)
ax.spines["bottom"].set_color("#BBBBBB")

# ─── 13. 保存与输出 ───────────────────────────────────────────
plt.tight_layout()
plt.savefig("main_eval_results.pdf", dpi=300, bbox_inches="tight")
plt.savefig("main_eval_results.png", dpi=300, bbox_inches="tight")
plt.show()
print("✔ Saved: main_eval_results.pdf  /  main_eval_results.png")