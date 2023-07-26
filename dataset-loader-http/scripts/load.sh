#!/usr/bin/env sh

set -xe

jupyter nbconvert --debug --to notebook --execute /content/src/load.ipynb --output /content/logs/load.ipynb
