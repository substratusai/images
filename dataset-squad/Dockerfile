FROM python:3.10

RUN mkdir /content
WORKDIR /content

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="$PATH:/content/scripts"

# Copy in build dependencies only since the build will take a while.
COPY ./scripts/ ./scripts
COPY ./src/ ./src
