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
docker run -it -v $(pwd)/artifacts:/content/artifacts \
  -v $(pwd)/load.ipynb:/content/load.ipynb -p 8888:8888 \
  dataset-squad notebook.sh

# In another terminal: Open browser.
open http://localhost:8888

# Now you can edit the contents of `src/`.
# Don't forget to re-build the container if you changed anything.
```

Fetch data.

```sh
docker run -e -v $(pwd)/artifacts:/content/artifacts squad-dataset

head data/*
```
