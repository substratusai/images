import json
import pytest
from .utils import filter_files


def test_filter_files():
    files = ["pytorch_model.bin", "tf_model.h5"]
    assert filter_files(files) == files[:1]

    files = ["config.json",
             "model-00001-of-00002.safetensors",
             "model-00002-of-00002.safetensors",
             "model.safetensors.index.json",
             "pytorch_model-00001-of-00002.bin",
             "pytorch_model-00002-of-00002.bin",
             "pytorch_model.bin.index.json"]
    assert filter_files(files) == [files[0], files[3], files[4], files[5], files[6]]


