#!/usr/bin/env bash

set -xe

if [[ -z "$NOTEBOOK" ]]; then
  for nb in /content/*.ipynb; do
    [ -e "$nb" ] || continue
    papermill $nb /content/artifacts/$(basename "$nb") --autosave-cell-every=1
  done
  for nb in /content/src/*.ipynb; do
    [ -e "$nb" ] || continue
    mkdir -p /content/artifacts/src
    papermill $nb /content/artifacts/src/$(basename "$nb") --autosave-cell-every=1
  done
else
  for nb in $NOTEBOOK; do
    [ -e "$nb" ] || continue
    papermill $nb /content/artifacts/$(basename "$nb") --autosave-cell-every=1
  done
fi