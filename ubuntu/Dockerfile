# TODO: Consider basing on ubuntu image, and install CUDA in this Dockerfile.
# https://gitlab.com/nvidia/container-images/cuda
FROM nvidia/cuda:12.2.0-runtime-ubuntu20.04

# Be explicit
USER root

# Setup apt-get
# https://www.cyberciti.biz/faq/explain-debian_frontend-apt-get-variable-for-ubuntu-debian/
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update

# Install Python
ARG PYTHON3_VERSION=3.12
RUN apt-get -y install python$PYTHON3_VERSION python3-pip

# Tini for signal handling, etc.
# https://github.com/krallin/tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Add "ml" user
#ARG USER=ml
#RUN useradd -ms /bin/bash $USER
#RUN usermod -aG sudo $USER
#RUN mkdir /home/$USER/scripts
#ENV PATH="$PATH:/home/ml/scripts"
## pip3 will install stuff here:
#ENV PATH="$PATH:/home/ml/.local/bin"
#WORKDIR /home/$USER
#USER $USER

# Using /content matches colab.
# Precreate some paths for convenience (when mounts are not present).
WORKDIR /content
ENV PATH="$PATH:/content/scripts"

RUN pip3 install jupyterlab

COPY scripts/* scripts/

CMD ["notebook.sh"]
