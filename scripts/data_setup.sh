#!/usr/bin/env bash
# Download one TEM1 image from our Borealis dataset into data/raw/.
#
# Only one image on purpose, to keep compute time reasonable: segmenting a
# single image with ADS takes about 15 minutes on CPU (on Mac at least), and the dataset has 142.
# Any other sample can be analyzed by changing FILE_NAME and FILE_ID (IDs are
# listed by the Borealis API for the dataset DOI below).
#
# Usage (from the repository root):
#     bash scripts/data_setup.sh

set -euo pipefail

SERVER_URL=https://demo.borealisdata.ca
# Dataset: doi:10.80240/FK2/IFEI6R (the download itself only needs the file ID)

FILE_NAME=data/raw/sub-nyuMouse11_sample-0006_TEM.png
FILE_ID=74037

mkdir -p "$(dirname "$FILE_NAME")"
curl -fL -o "$FILE_NAME" "$SERVER_URL/api/access/datafile/$FILE_ID"
