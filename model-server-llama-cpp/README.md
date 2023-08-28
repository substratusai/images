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
curl -L -o model-ggml.bin https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q2_K.bin
```

Convert the model to GGUF with this [script](https://github.com/ggerganov/llama.cpp/blob/master/convert-llama-ggmlv3-to-gguf.py):
```bash
convert-llama-ggmlv3-to-gguf.py --input model-ggml.bin --output model.bin
```

Run the image with that model:
```bash
docker run --gpus=all -d -p 8080:8080 --security-opt seccomp=unconfined  \
  -v $PWD/model.bin:/content/saved-model/model.bin --cap-add SYS_RESOURCE \
  -e USE_MLOCK=0 -e MODEL=/content/saved-model/model.bin \
  -e N_GPU_LAYERS=30 llama-cpp
```
Note that `N_GPU_LAYERS` will cause it to load 30 layers to the GPU. You can increase
that number from `30` to something more if you have more GPU memory available.

Verify it's working:
```bash
curl http://localhost:8080/v1/completions \
  -H "Content-Type: application/json" \
  -d '{ "prompt": "Who was the first president of the United States?", "stop": ["."]}'
```

You can also run a OpenAI compatible UI to test it out:
```bash
docker run -e OPENAI_API_KEY=notused -e OPENAI_API_HOST=http://localhost:8080 \
  --net=host -p 3000:3000 ghcr.io/mckaywrigley/chatbot-ui:main
```
