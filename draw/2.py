import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

# ─── Data: sorted by w/ CoT accuracy descending ───────────────────────
# (display_name, w/o CoT %, w/ CoT %, model_family)
data = [
    # ── Closed-Source API Models (28) ─────────────────────────────────
    ("DeepSeek-V3.2",              55.4, 76.4, "DeepSeek"),
    ("Claude-Sonnet-4.5",          76.0, 76.2, "Claude"),
    ("DeepSeek-V3.1",              53.6, 72.4, "DeepSeek"),
    ("Claude-Sonnet-4",            67.8, 71.2, "Claude"),
    ("Kimi-K2",                    50.8, 68.0, "Kimi"),
    ("GPT-4",                       8.6, 67.6, "GPT"),
    ("GPT-4.1-mini",                5.6, 65.2, "GPT"),
    ("Qwen3-Next-80B",              8.2, 63.8, "Qwen"),
    ("Qwen3-Coder-480B",            5.2, 63.8, "Qwen"),
    ("Qwen3-235B",                  8.6, 62.6, "Qwen"),
    ("Claude-Sonnet-3.7",          11.4, 62.6, "Claude"),
    ("Grok-4",                     60.0, 59.4, "Grok"),
    ("DeepSeek-V3.2-Thinking",     63.0, 58.4, "DeepSeek"),
    ("Gemini-3-Flash",             52.0, 53.8, "Gemini"),
    ("Qwen3-32B",                   4.4, 47.2, "Qwen"),
    ("GPT-4o",                      7.2, 47.0, "GPT"),
    ("MiniMax-M1-80k",             35.0, 43.4, "MiniMax"),
    ("Qwen2.5-72B",                 5.6, 33.4, "Qwen"),
    ("GPT-3.5-Turbo",               7.6, 31.2, "GPT"),
    ("Gemini-2.5-Flash",           37.6, 29.0, "Gemini"),
    ("GLM-5",                      23.4, 28.4, "GLM"),
    ("GLM-4.5",                    45.4, 26.0, "GLM"),
    ("Gemini-2.0-Flash",           20.2, 25.6, "Gemini"),
    ("MiniMax-M2",                 26.0, 24.2, "MiniMax"),
    ("MiniMax-M2.5",               26.0, 24.2, "MiniMax"),
    ("Qwen2.5-Coder-7B-Inst",       3.6, 10.4, "Qwen"),
    ("GLM-4-Flash",                 4.6,  8.6, "GLM"),
    ("Qwen2.5-Coder-7B",            4.2,  6.4, "Qwen"),
    # ── Open-Source Code Models (10) ──────────────────────────────────
    ("CodeReasoner-7b",             2.8, 15.2, "Open-Source"),
    ("CodeIO",                      3.4,  4.8, "Open-Source"),
    ("deepseek-coder-6.7b",         2.6,  4.0, "Open-Source"),
    ("starcoder2-7b",               2.2,  3.0, "Open-Source"),
    ("CodeLlama-34b",               3.4,  3.0, "Open-Source"),
    ("deepseek-coder-33b",          3.6,  2.8, "Open-Source"),
    ("gemma-7b",                    2.6,  2.8, "Open-Source"),
    ("starcoder2-15b",              3.4,  2.2, "Open-Source"),
    ("CodeLlama-13b",               3.2,  2.2, "Open-Source"),
    ("codegemma-7b",                2.6,  1.6, "Open-Source"),
]

# ─── Model family color palette ───────────────────────────────────────
COLORS = {
    "Claude":       "#E07B39",
    "DeepSeek":     "#2979FF",
    "GPT":          "#2E7D32",
    "Qwen":         "#7B1FA2",
    "Gemini":       "#0097A7",
    "GLM":          "#5D4037",
    "MiniMax":      "#C2185B",
    "Grok":         "#7CB342",
    "Kimi":         "#F4511E",
    "Open-Source":  "#546E7A",
}

# ─── Unpack ────────────────────────────────────────────────────────────
n        = len(data)
N_CLOSED = 28
names    = [d[0] for d in data]
acc_wo   = np.array([d[1] for d in data])
acc_wt   = np.array([d[2] for d in data])
fams     = [d[3] for d in data]
y        = np.arange(n)

BH  = 0.33   # bar height
GAP = 0.06   # gap between twin bars

# ─── Canvas ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 16))

# ── Section background ────────────────────────────────────────────────
ax.axhspan(-0.5, N_CLOSED - 0.5, facecolor="#EDF3FB", alpha=0.65, zorder=0)
ax.axhspan(N_CLOSED - 0.5, n - 0.5, facecolor="#FBF0ED", alpha=0.65, zorder=0)

# ── Alternating row tint for readability ──────────────────────────────
for i in range(n):
    if i % 2 == 0:
        ax.axhspan(i - 0.5, i + 0.5,
                   facecolor="#F4F4F4", alpha=0.35, zorder=0)

# ── X grid ────────────────────────────────────────────────────────────
ax.xaxis.grid(True, linestyle="--", color="#CCCCCC",
              alpha=0.55, linewidth=0.7, zorder=1)
ax.set_axisbelow(True)

# ── Draw grouped bars ─────────────────────────────────────────────────
for i in range(n):
    c  = COLORS.get(fams[i], "#888888")
    wo = acc_wo[i]
    wt = acc_wt[i]

    # w/ CoT  ── upper slot, full saturation
    ax.barh(y[i] - (BH / 2 + GAP / 2), wt,
            height=BH, color=c, alpha=0.88,
            zorder=2, linewidth=0)

    # w/o CoT ── lower slot, desaturated
    ax.barh(y[i] + (BH / 2 + GAP / 2), wo,
            height=BH, color=c, alpha=0.32,
            zorder=2, linewidth=0)

    # Numeric label (w/ CoT value, right of the longer bar)
    x_ann = max(wo, wt) + 0.5
    ax.text(x_ann, y[i], f"{wt:.1f}",
            va="center", ha="left",
            fontsize=12, color="#333333")

# ── Closed / Open divider ─────────────────────────────────────────────
ax.axhline(N_CLOSED - 0.5,
           color="#777777", linewidth=1.2, linestyle="--", zorder=3)

# ── Section annotation boxes ──────────────────────────────────────────
_box_kw = dict(boxstyle="round,pad=0.35", linewidth=0.8, alpha=0.92)

ax.text(84, (N_CLOSED - 1) / 2,
        "Closed-Source\nAPI Models",
        va="center", ha="center",
        fontsize=15, color="#1E3A6E", style="italic",
        bbox=dict(facecolor="white", edgecolor="#AACCEE", **_box_kw))

ax.text(84, N_CLOSED + (n - N_CLOSED - 1) / 2,
        "Open-Source\nCode Models",
        va="center", ha="center",
        fontsize=15, color="#6B2112", style="italic",
        bbox=dict(facecolor="white", edgecolor="#EECCAA", **_box_kw))

# ── Y axis ────────────────────────────────────────────────────────────
ax.set_yticks(y)
ax.set_yticklabels(names, fontsize=15)
ax.invert_yaxis()
ax.tick_params(axis="y", left=False, pad=4)

# ── X axis ────────────────────────────────────────────────────────────
ax.set_xlabel("Accuracy (%)", fontsize=17, labelpad=7, color="#444444")
ax.set_xlim(0, 96)
ax.set_xticks(range(0, 81, 10))
ax.tick_params(axis="x", colors="#666666")

# ── Spines ────────────────────────────────────────────────────────────
for sp in ["top", "right", "left"]:
    ax.spines[sp].set_visible(False)
ax.spines["bottom"].set_color("#BBBBBB")

# ── Legend ────────────────────────────────────────────────────────────
bar_patches = [
    mpatches.Patch(facecolor="#555555", alpha=0.88,
                   label="w/ CoT Prompting"),
    mpatches.Patch(facecolor="#555555", alpha=0.32,
                   label="w/o CoT Prompting"),
]
sep = mpatches.Patch(visible=False, label=" ")
fam_patches = [
    mpatches.Patch(facecolor=c, alpha=0.88, label=fam)
    for fam, c in COLORS.items()
]
ax.legend(
    handles=bar_patches + [sep] + fam_patches,
    fontsize=15, loc="lower right",
    ncol=2, framealpha=0.93,
    edgecolor="#CCCCCC", borderpad=0.9,
).get_frame().set_linewidth(0.7)

# ── Title ─────────────────────────────────────────────────────────────
ax.set_title(
    "Effect of Chain-of-Thought Prompting on Code Reasoning Accuracy",
    fontsize=18, fontweight="bold", pad=13, color="#1A1A1A",
)

plt.tight_layout()
plt.savefig("experiment2_cot_effect.pdf", dpi=300, bbox_inches="tight")
plt.savefig("experiment2_cot_effect.png", dpi=300, bbox_inches="tight")
plt.show()
print("✔ Saved: experiment2_cot_effect.pdf / .png")