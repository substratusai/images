ARG BASE_IMAGE=substratusai/base:latest
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04 as build

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    apt-get -y --no-install-recommends install \
      python3 python3-pip python3-venv git build-essential gcc wget && \
    mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /build
WORKDIR /build
RUN git clone https://github.com/ggerganov/llama.cpp.git
RUN cd llama.cpp  && make quantize

FROM ${BASE_IMAGE}

RUN mkdir -p /content/src /content/data /content/bin
WORKDIR /content

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/ggerganov/llama.cpp.git
RUN pip install --no-cache-dir -r llama.cpp/requirements.txt
COPY --from=build /build/llama.cpp/quantize /content/bin

ENV PATH="$PATH:/content/scripts:/content/bin"

# Copy in build dependencies only since the build will take a while.
COPY ./scripts/ ./scripts
COPY ./src/ ./src

ENTRYPOINT ["/tini", "--", "/content/scripts/entrypoint.sh"]
CMD convert.sh
