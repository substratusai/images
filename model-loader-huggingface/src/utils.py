from typing import List

def filter_pytorch_model(files: List[str]) -> List[str]:
    return list(filter(lambda f: not f.startswith("pytorch_model") and not f == "pytorch_model.bin.index.json", files))

def filter_tensorflow_model(files: List[str]) -> List[str]:
    return list(filter(lambda f: not f.startswith("tf_model") and not f == "tf_model.h5.index.json", files))

def filter_flax_model(files: List[str]) -> List[str]:
    return list(filter(lambda f: not f.startswith("flax_model") and not f == "flax_model.msgpack.index.json", files))


def filter_files(files: List[str]) -> List[str]:
    files = list(filter(lambda f: not f.startswith("coreml/"), files))
    has_pytorch_model = any([f.startswith("pytorch_model") for f in files])
    has_tensorflow_model = any([f.startswith("tf_model") for f in files])
    has_safetensors = any([f.endswith(".safetensors") for f in files])
    if has_safetensors:
        files = filter_pytorch_model(files)
        files = filter_tensorflow_model(files)
        files = filter_flax_model(files)
        return files
    if has_pytorch_model:
        files = filter_tensorflow_model(files)
        files = filter_flax_model(files)
        return files
    if has_tensorflow_model:
        files = filter_flax_model(files)
        return files
    return files

