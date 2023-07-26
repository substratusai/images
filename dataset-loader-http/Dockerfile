ARG BASE_IMAGE=substratusai/base:latest
FROM ${BASE_IMAGE}


RUN mkdir -p /content/src /content/data
WORKDIR /content

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="$PATH:/content/bin"

# Copy in build dependencies only since the build will take a while.
COPY ./scripts/ ./scripts
COPY ./src/ ./src

CMD load.sh
