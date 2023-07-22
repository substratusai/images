# Dataset HTTP loader

Load existing JSONL files into Substratus

A dataset that has instructions to write K8s YAML files

## Usage

Build.

```sh
docker build -t dataset-http-loader .
```

Explore and develop with a Jupyter Lab:
```sh
# Run a Jupyter Notebook.
docker run -it -v $(pwd)/src:/content/src -p 8888:8888 \
  -e PARAM_URLS=https://huggingface.co/datasets/substratusai/k8s-instructions/raw/main/k8s-instructions.jsonl \
  dataset-http-loader notebook.sh
```
Now open your browser at http://localhost:8888
