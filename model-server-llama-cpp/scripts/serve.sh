#!/usr/bin/env sh

set -xe

ls ${MODEL_DIR}
export MODEL=$(find "${MODEL_DIR}" -type f -iname "*.bin" | head -n 1)
PYTHONUNBUFFERED=1 python3 -m llama_cpp.server
