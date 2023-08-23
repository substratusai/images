ARG BASE_IMAGE=substratusai/base:latest
FROM ${BASE_IMAGE}

ENV MODEL_DIR="/content/saved-model"
ENV HOST=0.0.0.0
ENV PORT=8080

WORKDIR /content

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    apt-get -y --no-install-recommends install \
      python3 python3-pip git build-essential gcc wget \
      ocl-icd-opencl-dev opencl-headers clinfo libclblast-dev libopenblas-dev && \
    mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

# setting build related env vars
ENV CUDA_DOCKER_ARCH=all
ENV LLAMA_CUBLAS=1

# Install depencencies
RUN python3 -m pip install --upgrade pip pytest cmake scikit-build setuptools fastapi uvicorn sse-starlette pydantic-settings

# Install llama-cpp-python (build with cuda)
RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

COPY scripts/ scripts/

CMD serve.sh
EXPOSE $PORT
