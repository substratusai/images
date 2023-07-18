FROM substratusai/base-ubuntu

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY scripts/* scripts
COPY src/* src/

CMD load.sh
