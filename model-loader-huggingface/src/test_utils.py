import json
import pytest
from .utils import filter_files


@pytest.mark.parametrize(
    "files, expected",
    [
        (
            [
                "pytorch_model.bin",
                "tf_model.h5",
            ],
            ["pytorch_model.bin"],
        ),
        (
            [
                "config.json",
                "model-00001-of-00002.safetensors",
                "model-00002-of-00002.safetensors",
                "model.safetensors.index.json",
                "pytorch_model-00001-of-00002.bin",
                "pytorch_model-00002-of-00002.bin",
                "pytorch_model.bin.index.json",
            ],
            [
                "config.json",
                "model-00001-of-00002.safetensors",
                "model-00002-of-00002.safetensors",
                "model.safetensors.index.json",
            ],
        ),
        (
            [
                "flax_model-00001-of-00005.msgpack",
                "flax_model.msgpack.index.json",
                "model-00001-of-00005.safetensors",
                "model-00002-of-00005.safetensors",
                "model.safetensors.index.json",
                "pytorch_model-00001-of-00005.bin",
                "pytorch_model.bin.index.json",
                "tf_model-00001-of-00005.h5",
                "tf_model.h5.index.json"
            ],
            [
                "model-00001-of-00005.safetensors",
                "model-00002-of-00005.safetensors",
                "model.safetensors.index.json",
            ]
        ),
    ],
)
def test_filter_files(files, expected):
    assert filter_files(files) == expected


