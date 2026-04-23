"""Generate Figure: Incongruence rate by venue type."""

from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    venue_types = [
        "Museums",
        "Beaches",
        "Religious Sites",
        "Bodies of Water",
        "Gardens",
        "Farms",
        "Waterfalls",
        "Nature & Wildlife Areas",
        "Zoological Gardens",
        "Historic Sites",
        "National Parks",
    ]
    rates = [26.3, 19.0, 19.8, 23.7, 17.4, 16.6, 18.0, 16.4, 21.6, 15.6, 12.8]

    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "xtick.labelsize": 8,
            "ytick.labelsize": 9,
        }
    )

    fig, ax = plt.subplots(figsize=(11.4, 5.0), dpi=300)
    bars = ax.bar(
        venue_types,
        rates,
        color="#59A14F",
        edgecolor="black",
        linewidth=0.6,
    )

    ax.set_title("Incongruence Rate by Venue Type")
    ax.set_xlabel("Venue Type")
    ax.set_ylabel("Incongruence Rate (%)")
    ax.set_ylim(0, max(rates) + 4)
    ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.6)

    plt.setp(ax.get_xticklabels(), rotation=35, ha="right")

    for bar, value in zip(bars, rates):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.4,
            f"{value:.1f}",
            ha="center",
            va="bottom",
        )

    fig.tight_layout()
    output_path = Path(__file__).resolve().parents[1] / "Paper" / "fig_venue_incongruence_rate.png"
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
