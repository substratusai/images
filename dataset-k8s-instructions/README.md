# Dataset: K8s Instructions

A dataset that has instructions to write K8s YAML files

## Usage

Build.

```sh
docker build -t dataset-k8s-instructions .
```

Explore and develop with a Jupyter Lab.

```sh
# Run a Jupyter Notebook.
docker run -it -v $(pwd)/data:/data -v $(pwd)/src:/content/src -p 8888:8888 dataset-k8s-instructions notebook.sh

# In another terminal: Open browser.
open http://localhost:8888

# Now you can edit the contents of `src/`.

# Re-build the container if you changed anything.
docker build -t dataset-k8s-instructions .
```