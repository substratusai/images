# FROM nvidia/cuda:11.7.1-devel-ubuntu22.04
FROM substratusai/base

RUN mkdir -p /content/saved-model /content/model /content/logs /content/data /content/src
WORKDIR /content

COPY requirements.txt /content/requirements.txt
RUN pip install --no-cache-dir -r /content/requirements.txt

COPY scripts/* ./scripts/
COPY src/* ./src/

CMD train.sh
