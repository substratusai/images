from .utils import parse_training_args

def test_parse_training_args():
    params = {"num_train_epochs": "1"}
    assert parse_training_args(params).num_train_epochs == 1.0

    params = {"num_train_epochs": "1", "max_steps": "5"}
    args = parse_training_args(params)
    assert args.num_train_epochs == 1.0
    assert args.max_steps == 5
    assert args.output_dir == "/content/model/checkpoints"
