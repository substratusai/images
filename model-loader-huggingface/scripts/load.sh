#!/usr/bin/env sh

set -xe

export HUGGING_FACE_HUB_TOKEN=$PARAM_HUGGING_FACE_HUB_TOKEN
jupyter nbconvert --debug --to notebook --execute /content/src/load.ipynb --output /content/logs/load.ipynb
