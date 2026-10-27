#!/usr/bin/env python3
"""
Segment axons and myelin on a TEM image with AxonDeepSeg (ADS).

ADS writes its masks next to the input image, so this script segments the
image and then moves the masks to the output folder, keeping the data folder
clean and all generated files in one place.

Outputs (in --output-dir):
    <image>_seg-axon.png        binary axon mask
    <image>_seg-myelin.png      binary myelin mask
    <image>_seg-axonmyelin.png  combined mask (axon=255, myelin=127)

Usage:
    python scripts/segment.py data/raw/sub-nyuMouse07_sample-0001_TEM.png
    python scripts/segment.py data/raw/image.png --output-dir results/segmentation --gpu-id 0
"""

import argparse
import shutil
import sys
from pathlib import Path

from AxonDeepSeg.segment import DEFAULT_MODEL_PATH, segment_images


def segment(image_path: Path, output_dir: Path, model_path: Path, gpu_id: int) -> list[Path]:
    """Run ADS on one image and return the paths of the masks it produced."""
    output_dir.mkdir(parents=True, exist_ok=True)

    segment_images(path_images=[image_path], path_model=model_path, gpu_id=gpu_id)

    # ADS may convert the input to grayscale first and add a "_grayscale" tag
    # to the file name, so we match any mask that starts with the image name.
    masks = sorted(image_path.parent.glob(f"{image_path.stem}*_seg-*.png"))
    moved = []
    for mask in masks:
        target = output_dir / mask.name
        shutil.move(str(mask), target)
        moved.append(target)

    # Remove the temporary grayscale copy ADS may have created, so the raw
    # data folder only contains the original downloaded files.
    for tmp in image_path.parent.glob(f"{image_path.stem}_grayscale.*"):
        tmp.unlink()
    return moved


def main():
    parser = argparse.ArgumentParser(description="Segment axons and myelin on a TEM image with ADS.")
    parser.add_argument("image", type=Path, help="Path to the TEM image to segment (.png or .tif)")
    parser.add_argument("--output-dir", type=Path, default=Path("results/segmentation"),
                        help="Folder where the masks are saved (default: results/segmentation)")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL_PATH,
                        help="Path to the ADS model folder (default: ADS generalist model)")
    parser.add_argument("--gpu-id", type=int, default=-1,
                        help="GPU to use, -1 for CPU (default: -1)")
    args = parser.parse_args()

    if not args.image.exists():
        sys.exit(f"Error: image not found: {args.image}")

    print(f"Segmenting {args.image} with model {args.model.name}...")
    masks = segment(args.image, args.output_dir, args.model, args.gpu_id)

    if not masks:
        sys.exit("Error: ADS did not produce any mask.")
    for mask in masks:
        print(f"  saved {mask}")


if __name__ == "__main__":
    main()
