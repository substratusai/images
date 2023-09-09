# Base Image

Intended to be used in the `FROM` block of other Dockerfiles.

OS: Ubuntu

Includes:

- Python 3
- CUDA
- Jupyter Lab

By default the base image will run any notebooks ending with `.ipynb` extension
that are stored inside the `/content` or `/content/src` directory. The outputs
of the notebooks will be stored to `/content/artifacts`

## Build the base image

```
docker build -t substratusai/base .
```

Test it out by placing a notebook in `/content` directory:
```
docker run -ti -v $(pwd)/test.ipynb:/content/test.ipynb \
  -v $(pwd)/artifacts:/content/artifacts \
  --security-opt seccomp=unconfined \
  substratusai/base bash
```
