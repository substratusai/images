ARG BASE_IMAGE=substratusai/base:latest
FROM ${BASE_IMAGE}


COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY scripts/* scripts
COPY src/* src/

ENTRYPOINT ["/tini", "--", "HUGGING_FACE_HUB_TOKEN=$PARAM_HUGGING_FACE_HUB_TOKEN"]
CMD load.sh
