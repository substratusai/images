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
