#!/usr/bin/env sh

set -xe

ls ${MODEL_DIR}
export MODEL=$(find "${MODEL_DIR}" -type f -iname "*.bin" | head -n 1)
# TODO figure out how to automatically set N_GPU_LAYERS when a GPU is available
export N_GPU_LAYERS="${PARAM_N_GPU_LAYERS:-${N_GPU_LAYERS:-0}}"
PYTHONUNBUFFERED=1 python3 -m llama_cpp.server
