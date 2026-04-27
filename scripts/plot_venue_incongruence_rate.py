"""Generate Figure: Incongruence rate by venue type."""

from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    venue_types = [
        "Museums",
        "Bodies of Water",
        "Zoological Gardens",
        "Religious Sites",
        "Beaches",
        "Waterfalls",
        "Gardens",
        "Farms",
        "Nature & Wildlife Areas",
        "Historic Sites",
        "National Parks",
    ]
    rates = [26.3, 23.7, 21.6, 19.8, 19.0, 18.0, 17.4, 16.6, 16.4, 15.6, 12.8]

    sorted_items = sorted(zip(rates, venue_types), reverse=True)
    sorted_rates, sorted_venue_types = zip(*sorted_items)

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

    fig, ax = plt.subplots(figsize=(7.0, 5.0), dpi=300)
    bars = ax.barh(
        sorted_venue_types,
        sorted_rates,
        color="#59A14F",
        edgecolor="black",
        linewidth=0.6,
        height=0.65,
    )

    ax.set_xlabel("Incongruence Rate (%)")
    ax.set_ylabel("Venue Type")
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.invert_yaxis()

    label_offset = max(sorted_rates) * 0.01 + 0.3
    for rate, bar in zip(sorted_rates, bars):
        ax.text(
            rate + label_offset,
            bar.get_y() + bar.get_height() / 2,
            f"{rate:.1f}%",
            va="center",
            ha="left",
            fontsize=12,
        )

    fig.tight_layout()
    output_folder = Path(__file__).resolve().parents[1] / "Paper"
    output_folder.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_folder / "fig_venue_incongruence_rate.png", dpi=300, bbox_inches="tight")
    fig.savefig(output_folder / "fig_venue_incongruence_rate.pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
