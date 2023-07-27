#!/usr/bin/env bash

export HUGGING_FACE_HUB_TOKEN=$PARAM_HUGGING_FACE_HUB_TOKEN

exec "$@"