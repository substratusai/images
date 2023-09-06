# Dataset Loader HTTP

Load existing files into Substratus by downloading using HTTP

## Usage

Build the image locally:

```sh
docker build -t gguf-converter .
```

Explore and develop with a Jupyter Lab:
```sh
# create test params.json
cat > params.json <<EOF
{"name": "test", "download_model_id": "lmsys/vicuna-13b-v1.5"}
EOF
# Run a Jupyter Notebook.
docker run -it -v $(pwd)/src:/content/src \
  -v $(pwd)/params.json:/content/params.json -p 8888:8888 \
  --security-opt seccomp=unconfined gguf-converter notebook.sh
```
Now open your browser at http://localhost:8888
