"""Generate Figure: Selected incongruence patterns by reviewer expertise."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    patterns = ["Conservative Rater", "Harsh Deflator"]
    novice = [27.4, 10.8]
    expert = [40.4, 4.2]

    plt.style.use("classic")
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans"],
            "font.size": 12,
            "axes.labelsize": 13,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "grid.linestyle": "--",
            "grid.linewidth": 0.5,
            "grid.alpha": 0.6,
            "legend.fontsize": 11,
        }
    )

    x = np.arange(len(patterns))
    width = 0.34

    fig, ax = plt.subplots(figsize=(7.0, 3.9), dpi=300)
    novice_bars = ax.bar(
        x - width / 2,
        novice,
        width,
        label="Novice",
        color="#4C78A8",
        edgecolor="black",
        linewidth=0.6,
    )
    expert_bars = ax.bar(
        x + width / 2,
        expert,
        width,
        label="Expert",
        color="#59A14F",
        edgecolor="black",
        linewidth=0.6,
    )

    ax.set_xlabel("Mismatch Pattern")
    ax.set_ylabel("Percentage")
    ax.set_xticks(x)
    ax.set_xticklabels(patterns)
    ax.set_ylim(0, 45)
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    ax.legend(loc="upper right", frameon=False)

    for bars in (novice_bars, expert_bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.8,
                f"{height:.1f}%",
                ha="center",
                va="bottom",
                fontsize=11,
            )

    fig.tight_layout()
    output_folder = Path(__file__).resolve().parents[1] / "Paper"
    output_folder.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_folder / "fig_reviewer_expertise_patterns.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_folder / "fig_reviewer_expertise_patterns.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()