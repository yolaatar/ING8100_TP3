# Team n<sup>o</sup> 3

# ING8100_TP3

Reproducible open science project built around the dataset our team published on Borealis in Lab 2.

## Contents

1. [Overview](#overview)
2. [Data Availability](#data-availability)
3. [Instructions for Replicators](#instructions-for-replicators)
4. [List of Exhibits](#list-of-exhibits)
5. [Requirements](#requirements)
6. [Code Description](#code-description)
7. [Folder Structure](#folder-structure)
8. [Continuous Integration](#continuous-integration)
9. [Contributing](#contributing)
10. [License](#license)

## Overview

**Research question:** in the splenium of the mouse corpus callosum, how are axon diameter and g-ratio distributed, and are larger axons relatively more or less myelinated than smaller ones?

Axons and myelin are segmented automatically with AxonDeepSeg (ADS) on TEM images from the dataset we published on Borealis in Lab 2. Per-axon morphometrics are then computed, cleaned and summarized. Results and their interpretation are in the **[report](report.md)**.

The repository contains everything needed to go from the raw data on Borealis to the figures in the report:

1. a script that downloads the data from Borealis,
2. a segmentation script (ADS),
3. a preprocessing script that computes and cleans per-axon morphometrics,
4. an analysis script that computes summary indicators and produces figures,
5. a Markdown report that ties it all together.

## Data Availability

- [x] All data are publicly available.
- [ ] Some data cannot be made publicly available.
- [ ] No data can be made publicly available.

The data is **not** committed to this repository. It is hosted on Borealis and is fetched by the download script.

### Data Sources

- **Dataset:** TEM Images of Corpus Callosum in Control and Cuprizone-Intoxicated Mice with Axon and Myelin Segmentations (re-deposit of DANDI:001436, Jelescu et al., NeuroImage 2016)
- **Filename:** data/raw/sub-nyuMouse11_sample-0006_TEM.png
- **Source:** Borealis, the Canadian Dataverse Repository
- **URL / DOI:** doi:10.80240/FK2/IFEI6R
- **Access date:** 2026-10-27
- **License:** CC-BY 4.0

### Statement about Rights

- [x] The authors have legitimate access to and permission to use the data used in this project.
- [ ] The authors have documented permission to redistribute/publish the data contained within this repository.

## Instructions for Replicators

All commands are run from the repository root, in bash (Git Bash on Windows).

```bash
# 1. Get the code
git clone https://github.com/yolaatar/ING8100_TP3.git
cd ING8100_TP3

# 2. Create the environment (Python 3.11/3.12 + AxonDeepSeg v5.5.0 + model)
bash scripts/setup_env.sh
source .venv/bin/activate        

# 3. Download the data from Borealis
bash scripts/data_setup.sh

# 4. Segment axons and myelin -> results/segmentation/
python scripts/segment.py data/raw/sub-nyuMouse11_sample-0006_TEM.png

# 5. Compute and clean morphometrics -> data/processed/
python scripts/morphometrics.py results/segmentation/*_seg-axon.png

# 6. Summary indicators and figures -> results/ and figures/
python scripts/analyze.py data/processed/*_morphometrics_clean.csv
```

`figures/` is committed because the report embeds it. Running step 6 overwrites it with identical figures.

## List of Exhibits

| Exhibit | Output file | Script | Note |
|---|---|---|---|
| Figure 1: distribution of axon diameters | `figures/axon_diameter_distribution.png` | `analyze.py` | Committed, embedded in the report |
| Figure 2: g-ratio vs axon diameter | `figures/g_ratio_vs_diameter.png` | `analyze.py` | Committed, embedded in the report |
| Table 1: summary indicators (all axons) | `results/summary_overall.csv` | `analyze.py` | Generated, not committed |
| Summary indicators per image | `results/summary_per_image.csv` | `analyze.py` | Generated, not committed |

## Requirements

### Software Requirements

- Python 3.11 or 3.12 (required by AxonDeepSeg)
- AxonDeepSeg v5.5.0, which brings PyTorch, nnU-Net, pandas, NumPy and Matplotlib
- Environment manager: Python `venv` (no Conda). Exact versions are exported in [`requirements.txt`](requirements.txt).
- `curl` for the download script

### Memory, Runtime and Storage Requirements

- Storage: about 2 GB for the virtual environment and the ADS model, plus about 6 MB for the image
- Runtime: about 15 min on CPU (MacBook) for the segmentation of one image; the other steps take a few seconds
- No GPU required (`segment.py --gpu-id 0` to use one)

## Code Description

| Script | Step | Input | Output |
|---|---|---|---|
| `scripts/setup_env.sh` | Environment | none | `.venv/`, `requirements.txt` |
| `scripts/data_setup.sh` | Download | Borealis API | `data/raw/*.png` |
| `scripts/segment.py` | Segmentation (ADS generalist model) | TEM image | `results/segmentation/*_seg-axon.png`, `*_seg-myelin.png` |
| `scripts/morphometrics.py` | **Preprocessing**: per-axon morphometrics, then cleaning (removes border axons, missing myelin, g-ratio outside ]0, 1[, diameter < 0.3 µm) | axon + myelin masks | `data/processed/*_morphometrics_raw.csv`, `*_clean.csv` |
| `scripts/analyze.py` | Analysis: indicators (mean/SD diameter and g-ratio, myelin thickness, diameter–g-ratio correlation) and figures | cleaned CSVs | `results/*.csv`, `figures/*.png` |

## Folder Structure

```
ING8100_TP3/
├── README.md
├── report.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── AI_Prompts.md
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml
├── data/                 # not committed, filled by the scripts
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── setup_env.sh
│   ├── data_setup.sh
│   ├── segment.py
│   ├── morphometrics.py
│   └── analyze.py
├── figures/              # committed, embedded in the report
└── results/              # not committed (segmentation masks, summary tables)
```

## Continuous Integration

A GitHub Actions workflow ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)) runs automatically every time a pull request is opened or updated, and on every push to `main`. It has three jobs:

| Job | What it checks |
|-----|----------------|
| Required repository files | `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and `AI_Prompts.md` exist |
| Lint | Python scripts pass [ruff](https://docs.astral.sh/ruff/), shell scripts pass [shellcheck](https://www.shellcheck.net/) |
| Analysis smoke test | `analyze.py` runs on synthetic morphometrics tables and produces the expected tables and figures |

The workflow does not install AxonDeepSeg (several GB with PyTorch), so the segmentation and morphometrics steps are validated by running the pipeline locally.

## Contributing

`main` is protected: every change goes through a pull request reviewed by at least one other team member. See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch naming convention and workflow, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for collaboration expectations.

## License

Code in this repository is released under the [MIT License](LICENSE). The dataset keeps the license under which it is published on Borealis.
