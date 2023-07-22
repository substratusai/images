FROM python:3.10

RUN mkdir -p /content/src /content/bin /content/data
WORKDIR /content

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="$PATH:/content/bin"

# Copy in build dependencies only since the build will take a while.
COPY ./bin/ ./bin
COPY ./src/ ./src

CMD load.sh
