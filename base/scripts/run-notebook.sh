#!/usr/bin/env bash


if [[ -z "$NOTEBOOK" ]]; then
  for nb in /content/*.ipynb; do
    jupyter nbconvert --debug --to notebook --execute $nb --output /content/artifacts/$(basename "$nb")
  done
  for nb in /content/src/*.ipynb; do
    mkdir -p /content/artifacts/src
    jupyter nbconvert --debug --to notebook --execute $nb --output /content/artifacts/src/$(basename "$nb")
  done
else
  for nb in $NOTEBOOK; do
    jupyter nbconvert --debug --to notebook --execute $NOTEBOOK --output /content/artifacts/$(basename "$NOTEBOOK")
  done
fi