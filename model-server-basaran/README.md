# Substratus ModelServer Basaran Image

This image can be used for a model server to serve huggingface models.

The image expects a huggingface model under the /content/model directory.

## Usage for testing

### Building
Build the image:
```sh
docker build -t substratusai/model-server-basaran .
```