# Dataset Loader HTTP

Load existing files into Substratus by downloading using HTTP

## Usage

Build the image locally:

```sh
docker build -t dataset-loader-http .
```

Explore and develop with a Jupyter Lab:
```sh
# Run a Jupyter Notebook.
docker run -it -v $(pwd)/src:/content/src -p 8888:8888 \
  -e PARAM_URLS=https://huggingface.co/datasets/substratusai/k8s-instructions/raw/main/k8s-instructions.jsonl \
  dataset-loader-http notebook.sh
```
Now open your browser at http://localhost:8888
