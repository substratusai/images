ARG BASE_IMAGE=substratusai/base:latest
FROM ${BASE_IMAGE}

RUN mkdir -p /content/model /content/logs /content/data /content/src
WORKDIR /content

COPY requirements.txt /content/requirements.txt
RUN pip install --no-cache-dir -r /content/requirements.txt

COPY scripts/* ./scripts/
COPY src/* ./src/

CMD train.sh
