# Team n<sup>o</sup> 3

# ING8100_TP3

Reproducible open science project built around the dataset our team published on Borealis in Lab 2.

> **Status:** work in progress. The repository is set up (license, contribution guidelines, code of conduct, branch protection). Scripts, environment and report are coming next and this README will be updated as they land.

## Contents

1. [Overview](#overview)
2. [Data Availability](#data-availability)
3. [Instructions for Replicators](#instructions-for-replicators)
4. [List of Exhibits](#list-of-exhibits)
5. [Requirements](#requirements)
6. [Code Description](#code-description)
7. [Folder Structure](#folder-structure)
8. [Contributing](#contributing)
9. [License](#license)

## Overview

**Research question:** _TODO: state the research question._

This repository will contain everything needed to go from the raw dataset on Borealis to the figures and summary indicators in our report:

1. a script that downloads the data from Borealis,
2. a preprocessing script that cleans it,
3. an analysis script that computes summary indicators and produces figures,
4. a Markdown report that ties it all together.

## Data Availability

- [x] All data are publicly available.
- [ ] Some data cannot be made publicly available.
- [ ] No data can be made publicly available.

The data is **not** committed to this repository. It is hosted on Borealis and is fetched by the download script.

### Data Sources

- **Filename:** _TODO: exact file name on Borealis_
- **Source:** Borealis, the Canadian Dataverse Repository
- **URL / DOI:** _TODO: Borealis DOI_
- **Access date:** _TODO_
- **Variable names:** _TODO_
- **License:** _TODO: license of the dataset on Borealis_

### Statement about Rights

- [x] The authors have legitimate access to and permission to use the data used in this project.
- [ ] The authors have documented permission to redistribute/publish the data contained within this repository.

## Instructions for Replicators

_TODO: will be completed once the environment and scripts are in place._

```bash
git clone https://github.com/yolaatar/ING8100_TP3.git
cd ING8100_TP3
```

## List of Exhibits

_TODO: figures and tables will be listed here._

| Exhibit name | Output filename | Script | Note |
|--------------|-----------------|--------|------|
|              |                 |        |      |

## Requirements

### Software Requirements

_TODO: Python version and packages (pandas, numpy, matplotlib), exported in the environment file._

### Memory, Runtime and Storage Requirements

_TODO_

## Code Description

_TODO_

## Folder Structure

Planned layout:

```
ING8100_TP3/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── AI_Prompts.md
├── environment.yml
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── download_data.py
│   ├── preprocess.py
│   └── analyze.py
├── notebooks/
├── figures/
└── results/
```

## Contributing

`main` is protected: every change goes through a pull request reviewed by at least one other team member. See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch naming convention and workflow, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for collaboration expectations.

## License

Code in this repository is released under the [MIT License](LICENSE). The dataset keeps the license under which it is published on Borealis.
