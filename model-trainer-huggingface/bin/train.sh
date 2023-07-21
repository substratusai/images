#!/usr/bin/env sh

set -xe

export HF_HUB_DISABLE_PROGRESS_BARS=1
jupyter nbconvert --debug --to notebook --execute /content/src/train.ipynb --output /content/logs/train.ipynb