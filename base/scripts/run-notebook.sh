#!/usr/bin/env bash

set -xe
papermill_flags=(--autosave-cell-every=1 --log-output --log-level DEBUG)
if [[ -z "$NOTEBOOK" ]]; then
  for nb in /content/*.ipynb; do
    [ -e "$nb" ] || continue
    papermill $nb /content/artifacts/$(basename "$nb") "${papermill_flags[@]}"
    jupyter nbconvert --to html /content/artifacts/$(basename "$nb")
  done
  for nb in /content/src/*.ipynb; do
    [ -e "$nb" ] || continue
    mkdir -p /content/artifacts/src
    papermill $nb /content/artifacts/src/$(basename "$nb") "${papermill_flags[@]}"
    jupyter nbconvert --to html /content/artifacts/src/$(basename "$nb")
  done
else
  for nb in $NOTEBOOK; do
    [ -e "$nb" ] || continue
    papermill $nb /content/artifacts/$(basename "$nb") "${papermill_flags[@]}"
    jupyter nbconvert --to html /content/artifacts/$(basename "$nb")
  done
fi