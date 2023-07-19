# Dataset: SQuAD 2.0

https://rajpurkar.github.io/SQuAD-explorer/

## Usage

Build image.

```sh
docker build -t substratusai/dataset-squad .
```

Explore and develop with a Jupyter Lab.

```sh
# Run a Jupyter Notebook.
docker run -it -v $(pwd)/data:/data -v $(pwd)/src:/dataset/src -p 8888:8888 dataset-squad notebook.sh

# In another terminal: Open browser.
open http://localhost:8888

# Now you can edit the contents of `src/`.
# Don't forget to re-build the container if you changed anything.
```

Fetch data.

```sh
docker run -e -v $(pwd)/data:/data -v $(pwd)/logs:/dataset/logs squad-dataset load.sh

head data/*
```
