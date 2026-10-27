#!/usr/bin/env python3
"""
Compute summary indicators and figures from the cleaned morphometrics.

Accepts one or several *_morphometrics_clean.csv files, so the same script
works on a single image or on the whole dataset.

Outputs:
    results/summary_per_image.csv   indicators for each image
    results/summary_overall.csv     indicators pooled over all axons
    figures/axon_diameter_distribution.png
    figures/gratio_vs_diameter.png

Usage:
    python scripts/analyze.py data/processed/*_morphometrics_clean.csv
"""

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.switch_backend("Agg")  # no display needed, figures are only saved to disk


def load(csv_paths: list[Path]) -> pd.DataFrame:
    """Concatenate the per-image tables, keeping track of the source image."""
    frames = []
    for path in csv_paths:
        df = pd.read_csv(path)
        df.insert(0, "image", path.name.replace("_morphometrics_clean.csv", ""))
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def indicators(df: pd.DataFrame) -> pd.Series:
    """Summary indicators describing the myelinated axon population."""
    return pd.Series({
        "n_axons": len(df),
        "axon_diameter_mean_um": df["axon_diameter_um"].mean(),
        "axon_diameter_std_um": df["axon_diameter_um"].std(),
        "g_ratio_mean": df["g_ratio"].mean(),
        "g_ratio_std": df["g_ratio"].std(),
        "myelin_thickness_mean_um": df["myelin_thickness_um"].mean(),
        # Pearson correlation between caliber and g-ratio: tells whether larger
        # axons are relatively less (positive) or more (negative) myelinated.
        "corr_diameter_gratio": df["axon_diameter_um"].corr(df["g_ratio"]),
    })


def plot_diameter_distribution(df: pd.DataFrame, out_path: Path):
    """Histogram of axon diameters, the main descriptor of a nerve's fiber population."""
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.hist(df["axon_diameter_um"], bins=40, color="#1f77b4", edgecolor="white")
    mean = df["axon_diameter_um"].mean()
    ax.axvline(mean, color="black", linestyle="--", linewidth=1, label=f"mean = {mean:.2f} µm")
    ax.set_xlabel("Axon diameter (µm)")
    ax.set_ylabel("Number of axons")
    ax.set_title(f"Distribution of axon diameters (n = {len(df)} myelinated axons)")
    ax.legend()
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_gratio_vs_diameter(df: pd.DataFrame, out_path: Path):
    """Scatter of g-ratio against axon diameter, with a linear fit to show the trend."""
    x, y = df["axon_diameter_um"], df["g_ratio"]
    slope, intercept = np.polyfit(x, y, deg=1)
    x_fit = np.linspace(x.min(), x.max(), 100)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    # Small, transparent points: with thousands of axons, overlapping points
    # would otherwise hide where most of the population lies.
    ax.scatter(x, y, s=6, alpha=0.3, color="#1f77b4", label="axons")
    ax.plot(x_fit, slope * x_fit + intercept, color="#d62728", linewidth=2,
            label=f"linear fit: g = {slope:.3f}·d + {intercept:.3f}  (r = {x.corr(y):.2f})")
    ax.set_xlabel("Axon diameter (µm)")
    ax.set_ylabel("g-ratio")
    ax.set_title("g-ratio as a function of axon diameter")
    ax.legend(loc="lower right")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Summary indicators and figures from cleaned morphometrics.")
    parser.add_argument("csv", type=Path, nargs="+", help="One or more *_morphometrics_clean.csv files")
    parser.add_argument("--results-dir", type=Path, default=Path("results"),
                        help="Folder for the summary tables (default: results)")
    parser.add_argument("--figures-dir", type=Path, default=Path("figures"),
                        help="Folder for the figures (default: figures)")
    args = parser.parse_args()

    df = load(args.csv)
    if df.empty:
        sys.exit("Error: no axon in the input files.")
    args.results_dir.mkdir(parents=True, exist_ok=True)
    args.figures_dir.mkdir(parents=True, exist_ok=True)

    per_image = df.groupby("image")[["axon_diameter_um", "g_ratio", "myelin_thickness_um"]].apply(indicators)
    overall = indicators(df)
    per_image.to_csv(args.results_dir / "summary_per_image.csv")
    overall.to_frame("value").to_csv(args.results_dir / "summary_overall.csv")

    print("Summary over all images:")
    print(overall.round(3).to_string())

    plot_diameter_distribution(df, args.figures_dir / "axon_diameter_distribution.png")
    plot_gratio_vs_diameter(df, args.figures_dir / "gratio_vs_diameter.png")
    print(f"\nTables saved in {args.results_dir}/, figures saved in {args.figures_dir}/")


if __name__ == "__main__":
    main()
