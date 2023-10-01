ARG BASE_IMAGE=substratusai/base:latest
FROM ${BASE_IMAGE}

RUN mkdir -p /content/model

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/* src/
