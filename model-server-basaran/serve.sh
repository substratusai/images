#!/usr/bin/env sh

set -xe

export SERVER_MODEL_NAME="$HOSTNAME"

PYTHONUNBUFFERED=1 python -m basaran
