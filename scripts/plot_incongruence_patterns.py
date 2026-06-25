"""Generate Figure: Distribution of six directional incongruence patterns."""

from pathlib import Path
import os
import tempfile

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "matplotlib")
)
import matplotlib.pyplot as plt


def main() -> None:
    patterns = [
        "Conservative Rater",
        "Obligatory 5-Star",
        "Frustrated Neutral",
        "Polite Inflator",
        "Harsh Deflator",
        "Punitive Rater",
    ]
    values = [38.4, 28.3, 16.9, 7.3, 5.3, 3.7]

    sorted_items = sorted(zip(values, patterns), reverse=True)
    sorted_values, sorted_patterns = zip(*sorted_items)

    plt.style.use("classic")
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans"],
            "font.size": 15,
            "axes.labelsize": 16,
            "xtick.labelsize": 14,
            "ytick.labelsize": 14,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "grid.linestyle": "--",
            "grid.linewidth": 0.5,
            "grid.alpha": 0.6,
        }
    )

    fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=300)
    bars = ax.barh(
        sorted_patterns,
        sorted_values,
        color="#4C78A8",
        edgecolor="black",
        linewidth=0.6,
        height=0.65,
    )

    ax.set_xlabel("Percentage of Incongruent Reviews")
    ax.set_ylabel("Incongruence Pattern")
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.invert_yaxis()

    label_offset = max(sorted_values) * 0.01 + 0.3
    for value, bar in zip(sorted_values, bars):
        ax.text(
            value + label_offset,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.1f}%",
            va="center",
            ha="left",
            fontsize=12,
        )

    fig.tight_layout()
    output_folder = Path(__file__).resolve().parents[1] / "outputs" / "figures"
    output_folder.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_folder / "fig_incongruence_patterns.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_folder / "fig_incongruence_patterns.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
