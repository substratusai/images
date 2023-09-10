#!/usr/bin/env bash

set -xe
if [[ -z "$NOTEBOOK" ]]; then
  for nb in /content/*.ipynb; do
    [ -e "$nb" ] || continue
    python3 scripts/run-notebook.py "$nb" "/content/artifacts/$(basename ${nb})"
    # jupyter nbconvert --to html /content/artifacts/$(basename "$nb")
  done
  for nb in /content/src/*.ipynb; do
    [ -e "$nb" ] || continue
    mkdir -p /content/artifacts/src
    python3 scripts/run-notebook.py "$nb" "/content/artifacts/src/$(basename ${nb})"
    # jupyter nbconvert --to html /content/artifacts//src/$(basename "$nb")
  done
else
  for nb in $NOTEBOOK; do
    [ -e "$nb" ] || continue
    python3 scripts/run-notebook.py "$nb" "/content/artifacts/$(basename ${nb})"
    # jupyter nbconvert --to html /content/artifacts/$(basename "$nb")
  done
fi