ARG BASE_IMAGE=substratusai/base:latest
FROM ${BASE_IMAGE}


COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./load.ipynb ./
