ARG BASE_IMAGE=substratusai/base:latest
ARG COMPUTE_TYPE=gpu
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04 as build
ARG COMPUTE_TYPE

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    apt-get -y --no-install-recommends install \
      python3 python3-pip python3-venv git build-essential gcc wget \
      ocl-icd-opencl-dev opencl-headers clinfo libclblast-dev libopenblas-dev && \
    mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd && \
    rm -rf /var/lib/apt/lists/*
# Ensures that the python and pip executables used
# in the image will be those from our virtualenv.
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# setting build related env vars
ENV CUDA_DOCKER_ARCH=all
ENV LLAMA_CUBLAS=1

# Install depencencies
RUN /venv/bin/python3 -m pip install --upgrade pip wheel pytest cmake scikit-build setuptools fastapi uvicorn sse-starlette pydantic-settings

RUN git clone --recurse-submodules https://github.com/abetlen/llama-cpp-python.git
WORKDIR /llama-cpp-python
RUN if [ "$COMPUTE_TYPE" = "gpu" ]; then make build.cuda; fi
RUN if [ "$COMPUTE_TYPE" = "cpu" ]; then make build.openblas; fi

FROM ${BASE_IMAGE}

WORKDIR /content
ENV USE_MLOCK=0
ENV MODEL_DIR="/content/saved-model"
ENV HOST=0.0.0.0
ENV PORT=8080
ENV PATH="/venv/bin:$PATH"
COPY --from=build /venv /venv
COPY --from=build /llama-cpp-python /llama-cpp-python
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    apt-get -y --no-install-recommends install \
      git wget \
      ocl-icd-libopencl1 clinfo libclblast1 libopenblas0 && \
    mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd && \
    rm -rf /var/lib/apt/lists/*


COPY scripts/ scripts/

CMD serve.sh
EXPOSE $PORT
