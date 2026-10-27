#!/usr/bin/env python3
"""
Compute per-axon morphometrics from ADS masks and clean the resulting table.

This is the preprocessing step of the pipeline: it turns the segmentation
masks into a tidy table (one row per axon) and removes axons whose
measurements cannot be trusted.

Outputs (in --output-dir):
    <image>_morphometrics_raw.csv    every axon detected by ADS
    <image>_morphometrics_clean.csv  axons kept for the analysis

Usage:
    python scripts/morphometrics.py results/segmentation/sub-nyuMouse07_sample-0001_TEM_seg-axon.png
    python scripts/morphometrics.py results/segmentation/image_seg-axon.png --pixel-size 0.00236
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from AxonDeepSeg.morphometrics.compute_morphometrics import get_axon_morphometrics
from PIL import Image

# TEM1 images are acquired at 2.36 nm/px; ADS expects micrometers per pixel.
TEM1_PIXEL_SIZE_UM = 0.00236

# Keep only the columns we use, with explicit units in their names so the
# CSV can be read without knowing ADS conventions.
COLUMNS = {
    "x0": "x_px",
    "y0": "y_px",
    "axon_diam": "axon_diameter_um",
    "myelin_thickness": "myelin_thickness_um",
    "g_ratio": "g_ratio",
    "axon_area": "axon_area_um2",
    "myelin_area": "myelin_area_um2",
    "eccentricity": "eccentricity",
    "image_border_touching": "touches_border",
}


def load_mask(path: Path) -> np.ndarray:
    """Load an ADS mask as a boolean array (ADS saves masks as 0/255 PNGs)."""
    return np.array(Image.open(path).convert("L")) > 127


def compute(axon_mask: Path, myelin_mask: Path, pixel_size: float) -> pd.DataFrame:
    """Run ADS morphometrics and return one row per detected axon."""
    df = get_axon_morphometrics(
        load_mask(axon_mask),
        im_myelin=load_mask(myelin_mask),
        pixel_size=pixel_size,
        # "circle" means the diameter is the equivalent circular diameter,
        # which is the standard way of reporting axon caliber in the literature.
        axon_shape="circle",
        return_border_info=True,
    )
    df = df[[c for c in COLUMNS if c in df.columns]].rename(columns=COLUMNS)
    df.insert(0, "axon_id", range(len(df)))
    return df


def clean(df: pd.DataFrame, min_diameter: float) -> pd.DataFrame:
    """Remove axons whose measurements are unreliable, and say why."""
    n_start = len(df)

    # Axons cut by the image border are only partially visible, so their
    # diameter and g-ratio would be underestimated.
    df = df[~df["touches_border"].fillna(True).astype(bool)]
    n_border = n_start - len(df)

    # A missing g-ratio means ADS found no myelin around the axon: either an
    # unmyelinated axon or a segmentation error. Both are out of scope here.
    df = df.dropna(subset=["g_ratio", "axon_diameter_um", "myelin_thickness_um"])
    n_missing = n_start - n_border - len(df)

    # A g-ratio is inner/outer radius, so it must be strictly between 0 and 1.
    # Tiny objects are almost always segmentation noise, not real axons.
    df = df[(df["g_ratio"] > 0) & (df["g_ratio"] < 1) & (df["axon_diameter_um"] >= min_diameter)]
    n_outliers = n_start - n_border - n_missing - len(df)

    print(f"  {n_start} axons detected")
    print(f"  - {n_border} touching the border")
    print(f"  - {n_missing} without myelin measurement")
    print(f"  - {n_outliers} outliers (g-ratio outside ]0, 1[ or diameter < {min_diameter} um)")
    print(f"  = {len(df)} axons kept")

    return df.drop(columns="touches_border").reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser(description="Compute and clean ADS morphometrics from segmentation masks.")
    parser.add_argument("axon_mask", type=Path, help="Path to the *_seg-axon.png mask produced by segment.py")
    parser.add_argument("--myelin-mask", type=Path, default=None,
                        help="Path to the *_seg-myelin.png mask (default: inferred from the axon mask name)")
    parser.add_argument("--pixel-size", type=float, default=TEM1_PIXEL_SIZE_UM,
                        help=f"Pixel size in micrometers (default: {TEM1_PIXEL_SIZE_UM}, TEM1)")
    parser.add_argument("--min-diameter", type=float, default=0.3,
                        help="Minimum axon diameter in micrometers (default: 0.3)")
    parser.add_argument("--output-dir", type=Path, default=Path("data/processed"),
                        help="Folder where the CSV files are saved (default: data/processed)")
    args = parser.parse_args()

    if "_seg-axon" not in args.axon_mask.name:
        sys.exit("Error: expected an ADS axon mask (file name containing '_seg-axon').")
    myelin_mask = args.myelin_mask or args.axon_mask.with_name(
        args.axon_mask.name.replace("_seg-axon", "_seg-myelin"))
    for path in (args.axon_mask, myelin_mask):
        if not path.exists():
            sys.exit(f"Error: mask not found: {path}")

    image_name = args.axon_mask.name.split("_seg-axon")[0]
    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Computing morphometrics for {image_name} (pixel size {args.pixel_size} um)...")
    raw = compute(args.axon_mask, myelin_mask, args.pixel_size)
    if raw.empty:
        sys.exit("Error: no axon found in the mask.")
    raw.to_csv(args.output_dir / f"{image_name}_morphometrics_raw.csv", index=False)

    cleaned = clean(raw, args.min_diameter)
    out_path = args.output_dir / f"{image_name}_morphometrics_clean.csv"
    cleaned.to_csv(out_path, index=False)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
