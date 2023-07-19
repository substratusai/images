FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

ENV MODEL="/content/saved-model"
ENV MODEL_LOCAL_FILES_ONLY="true"
ENV MODEL_LOAD_IN_8BIT="true"
ENV MODEL_TRUST_REMOTE_CODE="true"
ENV PORT=8080
ENV PATH="$PATH:/content/scripts"

WORKDIR /content

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    apt-get -y --no-install-recommends install python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY scripts/ scripts/

CMD serve.sh
EXPOSE $PORT
