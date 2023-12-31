# TODO: Consider basing on ubuntu image, and install CUDA in this Dockerfile.
# https://gitlab.com/nvidia/container-images/cuda
FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# Be explicit
USER root

# Setup apt-get
# https://www.cyberciti.biz/faq/explain-debian_frontend-apt-get-variable-for-ubuntu-debian/
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -y --no-install-recommends install python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*


# Using /content matches colab.
# Precreate some paths for convenience (when mounts are not present).
WORKDIR /content
RUN mkdir -p /content/artifacts

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY scripts/* /usr/local/bin/

# Tini for signal handling, etc.
# https://github.com/krallin/tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

CMD ["run-notebook.sh"]
