"""Render the report's evidence figures from committed machine-readable data."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


REPORT = Path("reports/packet-scheduling-claim-audit-2026-07-23")
DATA = json.loads((REPORT / "data/evidence.json").read_text(encoding="utf-8"))
IMAGES = REPORT / "images"

NAVY = "#17324d"
BLUE = "#2f6f9f"
TEAL = "#2a9d8f"
ORANGE = "#e76f51"
GOLD = "#e9c46a"
GRAY = "#6b7280"


def _finish(name: str) -> None:
    plt.tight_layout()
    plt.savefig(IMAGES / name, dpi=170, bbox_inches="tight", facecolor="white")
    plt.close()


def claim_3_headline() -> None:
    row = DATA["claim_3"]
    horizon = np.array(row["horizon"], dtype=float)
    regret = np.array(row["regret"], dtype=float)
    positive_mask = regret > 0
    positive_horizon = horizon[positive_mask]
    positive = regret[positive_mask]
    reference = positive[-1] * np.sqrt(positive_horizon / positive_horizon[-1])
    plt.figure(figsize=(8.8, 4.8))
    plt.loglog(positive_horizon, positive, "o-", color=ORANGE, linewidth=2.7, label="observed positive theta-regret")
    plt.loglog(positive_horizon, reference, "--", color=GRAY, linewidth=2.0, label="sqrt(T) reference")
    for x, y in zip(positive_horizon, positive):
        plt.annotate(f"{y:,.1f}", (x, y), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=9)
    plt.title("Claim 3: bounded-reward counterexample grows faster than √T", loc="left", color=NAVY, weight="bold")
    plt.xlabel("horizon T (log scale)")
    plt.ylabel("positive theta₃-regret (log scale)")
    plt.grid(alpha=0.2, which="both")
    plt.legend(frameon=False)
    plt.figtext(0.99, 0.01, f"last-doubling slope = {row['last_loglog_slope']:.3f}", ha="right", color=GRAY)
    _finish("01-claim-3-linear-regret.png")


def claim_2_counterexample() -> None:
    row = DATA["claim_2"]
    plt.figure(figsize=(7.6, 4.6))
    bars = plt.bar(["ALG$^\\theta$", "Independent OPT"], [row["algorithm_gain"], row["offline_gain"]], color=[BLUE, ORANGE], width=0.58)
    for bar, value in zip(bars, [row["algorithm_gain"], row["offline_gain"]]):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 0.2, f"{value:g}", ha="center", weight="bold")
    plt.ylim(0, 9.2)
    plt.ylabel("scheduled reward")
    plt.title("Claim 2: the six-packet instance exceeds θ₃", loc="left", color=NAVY, weight="bold")
    plt.text(0.5, 0.82, f"OPT / ALG = {row['ratio']:.1f}  >  θ₃ = {row['theta_3']:.1f}", transform=plt.gca().transAxes, ha="center", bbox={"boxstyle": "round,pad=0.4", "fc": "#fff4e8", "ec": ORANGE})
    plt.grid(axis="y", alpha=0.2)
    _finish("02-claim-2-counterexample.png")


def competitive_models() -> None:
    row = DATA["competitive_models"]
    x = np.arange(len(row["claims"]))
    width = 0.24
    plt.figure(figsize=(9.2, 4.8))
    plt.bar(x - width, row["exact_max_ratio"], width, label="exact bounded model", color=BLUE)
    plt.bar(x, row["falsification_search_max_ratio"], width, label="broad search maximum", color=TEAL)
    plt.bar(x + width, row["paper_alpha"], width, label="paper α", color=GOLD)
    plt.xticks(x, row["claims"])
    plt.ylim(1.0, 1.72)
    plt.ylabel("OPT / expected ALG")
    plt.title("Competitive cores align, but finite maxima do not prove regret theorems", loc="left", color=NAVY, weight="bold")
    plt.grid(axis="y", alpha=0.2)
    plt.legend(frameon=False, ncol=3, loc="upper center")
    _finish("03-competitive-core-maxima.png")


def stress_diagnostics() -> None:
    row = DATA["stress"]
    horizon = row["horizon"]
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.3))
    axes[0].plot(horizon, row["claim_4_regret_over_sqrt_KT"], "o-", color=BLUE, linewidth=2.4)
    axes[0].axhline(0, color=GRAY, linewidth=1)
    axes[0].set_xscale("log", base=2)
    axes[0].set_title("Claim 4: 5/4-regret / √KT")
    axes[0].set_xlabel("T")
    axes[0].set_ylabel("normalized regret")
    axes[0].grid(alpha=0.2)
    axes[1].plot(horizon, row["claim_5_beta_sum_over_sqrt_KT"], "o-", color=TEAL, linewidth=2.4)
    axes[1].set_xscale("log", base=2)
    axes[1].set_title("Claim 5: selected width sum / √KT")
    axes[1].set_xlabel("T")
    axes[1].set_ylabel("normalized width sum")
    axes[1].grid(alpha=0.2)
    fig.suptitle("Long-horizon diagnostics remain bounded on faithful stress families", x=0.02, ha="left", color=NAVY, weight="bold")
    _finish("04-long-horizon-diagnostics.png")


def route_matrix() -> None:
    row = DATA["route_matrix"]
    values = np.array(row["values"])
    fig, ax = plt.subplots(figsize=(9.2, 3.7))
    image = ax.imshow(
        values,
        cmap=ListedColormap(["#f4a3a8", "#fff3b0", "#b8d8f0"]),
        vmin=0,
        vmax=2,
        aspect="auto",
    )
    ax.set_xticks(np.arange(len(row["routes"])), labels=row["routes"])
    ax.set_yticks(np.arange(len(row["claims"])), labels=row["claims"])
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            ax.text(j, i, row["labels"][i][j], ha="center", va="center", color=NAVY, weight="bold", fontsize=9)
    ax.set_title("Four materially different routes per unresolved claim", loc="left", color=NAVY, weight="bold")
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
    for edge in ax.spines.values():
        edge.set_visible(False)
    image.set_clim(0, 2)
    _finish("05-route-matrix.png")


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    claim_3_headline()
    claim_2_counterexample()
    competitive_models()
    stress_diagnostics()
    route_matrix()
    for path in sorted(IMAGES.glob("*.png")):
        print(path)


if __name__ == "__main__":
    main()
