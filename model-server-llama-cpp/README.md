# Substratus Server Llama.cpp

This image can be used to serve models that are in GGML format.

The image expects a single GGML model as a single bin file under the /content/saved-model/ directory.

## Usage for testing

### Building
Build the image:
```sh
docker build -t substratusai/model-server-llama-cpp .
```
