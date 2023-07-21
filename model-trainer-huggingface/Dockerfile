FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

ENV PATH="$PATH:/content/bin"
RUN mkdir -p /content/saved-model /content/model /content/logs /content/data /content/src
WORKDIR /content

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    apt-get -y --no-install-recommends install python3 python3-pip git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /content/requirements.txt
RUN pip install --no-cache-dir -r /content/requirements.txt

COPY bin/* ./bin/
COPY src/* ./src/

CMD train.sh
