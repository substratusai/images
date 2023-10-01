# Substratus HuggingFace Model Trainer

This image fine tunes large language models from HuggingFace. It's using PEFT
such that it can fine tune even 40 billion parameter models on a few L4 GPUs.

The image expects a huggingface model under the /content/model directory.

## Usage

Currently this image supports all HuggingFace transformer.TrainingArguments that
you pass through Substratus `params` in the `Model` resource.

See the TrainingArguments docs for available arguments: [TrainingArguments](https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments)

For example, if you wish to pass num_train_epochs, you can create a Model resource
specifying the params. Below is an example Model resource that sets TrainingArguments:
```
apiVersion: substratus.ai/v1
kind: Model
metadata:
  name: falcon-7b-instruct-k8s
spec:
  image:
    name: substratusai/model-trainer-huggingface
  model:
    name: falcon-7b-instruct
  dataset:
    name: k8s-instructions
  params:
    num_train_epochs: 1
    per_device_train_batch_size: 1
    logging_first_step: True
    optim: paged_adamw_32bit
  resources:
    gpu:
      count: 4
      type: nvidia-l4
```

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
