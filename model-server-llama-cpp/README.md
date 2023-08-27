# Substratus Server Llama.cpp

This image can be used to serve models that are in GGML format.

The image expects a single GGML model as a single bin file under the /content/saved-model/ directory.

## Usage for testing

### Building
Build the image:
```sh
docker build -t llama-cpp .
```

### Testing
Download a GGML model:
```bash
curl -L -o model.bin https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q2_K.bin
```

Run the image with that model:
```bash
docker run --gpus=all -d -p 8080:8080 \
  -v $PWD/model.bin:/content/saved-model/model.bin llama-cpp
```

Verify it's working:
```bash
curl http://localhost:8080/v1/completions \
  -H "Content-Type: application/json" \
  -d '{ "prompt": "Who was the first president of the United States?", "stop": ["."]}'
```
