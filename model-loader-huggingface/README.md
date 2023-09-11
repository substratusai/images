# Substratus HuggingFace Model Loader

This loader loads models from HuggingFace into Substratus. The model is downloaded
by getting the download URL from each file in the model repo and using native
Python libraries for multi threading and downloads.

The container image expects the following parameters:
```
name: The name of the HuggingFace model to load. The default is "tiiuae/falcon-7b-instruct"
```

## Local Development

```sh
docker build . -t substratusai/model-loader-huggingface
cat > params.json <<EOF
{"name": "facebook/opt-125m"}
EOF
docker run -it \
  -v $(pwd)/src:/content/src \
  -v $(pwd)/params.json:/content/params.json \
  -v $(pwd)/artifacts:/content/artifacts \
  -p 8888:8888 \
  substratusai/model-loader-huggingface notebook.sh
```

Open Notebook at [http://localhost:8888](http://localhost:8888?token=default).

## Local Loading

```sh
cat > params.json <<EOF
{"name": "facebook/opt-125m"}
EOF
docker run -it \
  -v $(pwd)/params.json:/content/params.json \
  -v $(pwd)/artifacts:/content/artifacts \
  substratusai/model-loader-huggingface
```

