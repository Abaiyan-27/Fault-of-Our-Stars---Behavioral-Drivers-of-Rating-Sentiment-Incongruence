"""Generate Figure: Distribution of six directional incongruence patterns."""

from pathlib import Path

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

    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
        }
    )

    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=300)
    bars = ax.bar(
        patterns,
        values,
        color="#4C78A8",
        edgecolor="black",
        linewidth=0.6,
    )

    ax.set_title("Distribution of Six Directional Incongruence Patterns")
    ax.set_xlabel("Incongruence Pattern")
    ax.set_ylabel("Percentage of Incongruent Reviews")
    ax.set_ylim(0, max(values) + 6)
    ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.6)

    plt.setp(ax.get_xticklabels(), rotation=25, ha="right")

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.6,
            f"{value:.1f}",
            ha="center",
            va="bottom",
        )

    fig.tight_layout()
    output_path = Path(__file__).resolve().parents[1] / "Paper" / "fig_incongruence_patterns.png"
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
