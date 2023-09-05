#!/usr/bin/env sh

set -xe

ls ${MODEL_DIR}
if [[ -z "$MODEL" ]]; then
  export MODEL=$(find "${MODEL_DIR}" -type f \( -name "*.bin" -o -name "*.gguf" \) | head -n 1)
fi

PYTHONUNBUFFERED=1 python3 -m llama_cpp.server
