# Substratus HuggingFace Model Trainer

This image fine tunes large language models from HuggingFace. It's using PEFT
such that it can fine tune even 40 billion parameter models on a few L4 GPUs.

The image expects a huggingface model under the /content/saved-model directory.

## Usage for testing

### Building
Build the image:
```sh
docker build -t substratusai/model-trainer-huggingface .
```

### Running notebook in container
This is helpful to test out the loader while developing

Run Jupyter Notebook mounting local src directory:
```
docker run -it -p 8888:8888 \
  -v $(pwd)/src:/content/src \
  substratusai/model-trainer-huggingface notebook.sh
```

You can then access Jupyter Lab by visiting:
[http://localhost:8888](http://localhost:8888).

You will see a notebook called train.ipynb under the src directory. You can modify that
that notebook as needed and run it to fine tune the model.
