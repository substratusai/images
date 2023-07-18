# Dataset: SQuAD 2.0

https://rajpurkar.github.io/SQuAD-explorer/

## Usage

Build.

```sh
docker build -t squad-dataset .
```

Explore and develop with a Jupyter Lab.

```sh
# Run a Jupyter Notebook.
docker run -it -e LOAD_DATA_PATH=/data/all.jsonl -v $(pwd)/data:/data -v $(pwd)/src:/dataset/src -p 8888:8888 squad-dataset notebook.sh

# In another terminal: Open browser.
open http://localhost:8888

# Now you can edit the contents of `src/`.

# Re-build the container if you changed anything.
docker build -t squad-dataset .
```

Fetch data.

```sh
docker run -e -v $(pwd)/data:/data -v $(pwd)/logs:/dataset/logs squad-dataset load.sh

head data/*
```
