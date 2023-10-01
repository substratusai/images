#!/usr/bin/env bash

set -e
if [[ -z "$NOTEBOOK" ]]; then
  for nb in /content/*.ipynb; do
    [ -e "$nb" ] || continue
    echo "Executing notebook $nb"
    run-notebook.py "$nb" "/content/artifacts/$(basename ${nb})" --cwd "$(dirname ${nb})"
  done
  for nb in /content/src/*.ipynb; do
    [ -e "$nb" ] || continue
    mkdir -p /content/artifacts/src
    echo "Executing notebook $nb"
    run-notebook.py "$nb" "/content/artifacts/src/$(basename ${nb})" --cwd "$(dirname ${nb})"
  done
else
  for nb in $NOTEBOOK; do
    [ -e "$nb" ] || continue
    echo "Executing notebook $nb"
    run-notebook.py "$nb" "/content/artifacts/$(basename ${nb})" --cwd "$(dirname ${nb})"
  done
fi