#!/usr/bin/env bash
# Create a Python virtual environment with AxonDeepSeg (ADS) and its dependencies.
#
# Usage (from the repository root, in bash / Git Bash on Windows):
#     bash scripts/setup_env.sh
#
# Then activate the environment:
#     source .venv/bin/activate        # macOS / Linux
#     source .venv/Scripts/activate    # Windows (Git Bash)

set -euo pipefail

# ADS is pinned to a release tag so everyone gets the exact same code and
# the same default model, which is what makes the segmentations reproducible.
ADS_VERSION="v5.5.0"
VENV_DIR=".venv"

# ADS only supports Python 3.11 and 3.12 (see its pyproject.toml), so we look
# for one of those explicitly instead of trusting whatever "python" points to.
PYTHON=""
for candidate in python3.11 python3.12 "py -3.11" "py -3.12" python3 python; do
    if $candidate -c 'import sys; sys.exit(0 if sys.version_info[:2] in [(3, 11), (3, 12)] else 1)' 2>/dev/null; then
        PYTHON="$candidate"
        break
    fi
done
if [ -z "$PYTHON" ]; then
    echo "Error: Python 3.11 or 3.12 is required by AxonDeepSeg but was not found." >&2
    exit 1
fi
echo "Using $($PYTHON --version)"

$PYTHON -m venv "$VENV_DIR"

# The venv layout differs between Windows (Scripts/) and macOS/Linux (bin/).
if [ -d "$VENV_DIR/Scripts" ]; then
    VENV_PY="$VENV_DIR/Scripts/python"
else
    VENV_PY="$VENV_DIR/bin/python"
fi

"$VENV_PY" -m pip install --upgrade pip
# Installing from the git tag pulls every runtime dependency declared by ADS
# (nnUNet, PyTorch, scikit-image, pandas, matplotlib...).
"$VENV_PY" -m pip install "git+https://github.com/axondeepseg/axondeepseg.git@${ADS_VERSION}"

# Download the default generalist model now, so the first segmentation does
# not fail halfway because of a network issue.
"$VENV_PY" -m AxonDeepSeg.download_model

# Export the exact versions that were installed, so the environment can be
# rebuilt later with: pip install -r requirements.txt
"$VENV_PY" -m pip freeze --exclude-editable > requirements.txt

echo
echo "Environment ready in $VENV_DIR (ADS $ADS_VERSION). Exact versions saved in requirements.txt."
