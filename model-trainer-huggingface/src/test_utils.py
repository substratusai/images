import json
import pytest
from .utils import parse_training_args


def test_parse_training_args_int_float():
    params = {"num_train_epochs": "1", "target_modules": "q,v"}
    assert parse_training_args(params).num_train_epochs == 1.0

    params = {"num_train_epochs": "1", "max_steps": "5"}
    args = parse_training_args(params)
    assert args.num_train_epochs == 1.0
    assert args.max_steps == 5
    assert args.output_dir == "/content/artifacts/checkpoints"

    params = {"num_train_epochs": "2.0", "max_steps": "5"}
    args = parse_training_args(params)
    assert args.num_train_epochs == 2.0
    assert args.max_steps == 5
    assert args.output_dir == "/content/artifacts/checkpoints"


def test_parse_training_args_bool():
    params = {"logging_first_step": "True"}
    args = parse_training_args(params)
    assert args.logging_first_step == True

    params = {"logging_first_step": "False"}
    args = parse_training_args(params)
    assert args.logging_first_step == False


def test_parse_training_args_bool_invalid():
    params = {"logging_first_step": "yes"}
    with pytest.raises(ValueError):
        args = parse_training_args(params)


def test_parse_training_args_str():
    params = {"logging_first_step": "True"}
    args = parse_training_args(params)
    assert args.logging_first_step == True

def test_parse_training_args_push_to_hub():
    params = {"push_to_hub": "substratusai/test-model"}
    args = parse_training_args(params)
    assert args.push_to_hub == False
