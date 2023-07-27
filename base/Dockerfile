# TODO: Consider basing on ubuntu image, and install CUDA in this Dockerfile.
# https://gitlab.com/nvidia/container-images/cuda
FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# Be explicit
USER root

# Setup apt-get
# https://www.cyberciti.biz/faq/explain-debian_frontend-apt-get-variable-for-ubuntu-debian/
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -y --no-install-recommends install \
    python3 \
    python3-pip \
    python3-dev \
    gcc \
    git \
    && \
    rm -rf /var/lib/apt/lists/*


# Using /content matches colab.
# Precreate some paths for convenience (when mounts are not present).
WORKDIR /content
ENV PATH="$PATH:/content/scripts"

RUN pip3 install --no-cache-dir jupyterlab

COPY scripts/* scripts/

# Tini for signal handling, etc.
# https://github.com/krallin/tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]


CMD ["notebook.sh"]
