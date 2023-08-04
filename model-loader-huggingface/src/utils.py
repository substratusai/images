from typing import List


def filter_files(files: List[str]) -> List[str]:
    files = list(filter(lambda f: not f.startswith("coreml/"), files))
    has_pytorch_model = any([f.startswith("pytorch_model") for f in files])
    if has_pytorch_model:
        # filter out safetensors
        files = list(filter(lambda f: not f.endswith(".safetensors"), files))
        # filter out tensorflow model
        files = list(filter(lambda f: not f.startswith("tf_model"), files))
    return files

