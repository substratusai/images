#!/usr/bin/env sh

set -xe

jupyter nbconvert --debug --to notebook --execute /content/src/convert.ipynb --output /content/logs/convert.ipynb
