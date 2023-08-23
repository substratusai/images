#!/usr/bin/env sh

set -xe

export SERVER_MODEL_NAME="$HOSTNAME"
export LOAD_IN_4BIT="${PARAM_LOAD_IN_4BIT:-false}"

# Backwards compatiblity to keep load in 8 bit the default
if [ "${LOAD_IN_4BIT}" = "false" ]; then
echo "Loading model in 8 bit mode"
export LOAD_IN_8BIT="true"
else
echo "Loading model in 4 bit mode"
fi

PYTHONUNBUFFERED=1 python -m basaran
