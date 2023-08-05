#!/usr/bin/env sh

set -xe

ENV SERVER_MODEL_NAME="$HOSTNAME"
PYTHONUNBUFFERED=1 python -m basaran
