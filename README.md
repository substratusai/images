# Substratus Images
This repository contains all the images that are known to work well within
Substratus.

The images all use the same base image located in the `base` directory.

## Build and Push Github Workflow
The container build and push pipeline builds and pushes container images
automatically to Docker Hub. For PRs, the images get tagged with the PR 
ID. Once a PR is merged into main the pipeline automatically builds
and pushes an image with the main tag. The latest tag
only gets updated once you push a tag using the
`vX.Y.Z` format, where `X`, `Y` and `Z` are numbers

For example, lets take the following image:
```
substratusai/model-trainer-huggingface
```

Once you create a PR and that PR has the id 5, then
the a container image will get pushed with the following
tag:
```
substratusai/model-trainer-huggingface:pr-5
```

Once that PR is merged into main, a container image with
the following tag gets pushed:
```
substratusai/model-trainer-huggingface:main
```

Finally once you create and push a tag like `v0.6.5` a container image
with the following tags would get pushed:
```
substratusai/model-trainer-huggingface:v0.6.5
substratusai/model-trainer-huggingface:latest
```
