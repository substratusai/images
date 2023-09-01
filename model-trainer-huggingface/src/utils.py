import typing
import inspect
import json

from transformers import TrainingArguments

ignore_training_args = set("push_to_hub")

def parse_training_args(params: typing.Mapping) -> TrainingArguments:
    typed_params = dict(
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        warmup_steps=2,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=1,
        output_dir="/content/model/checkpoints",
        optim="paged_adamw_32bit",
    )

    training_parameters = inspect.signature(TrainingArguments.__init__).parameters
    for k, v in training_parameters.items():
        if k in params and k not in ignore_training_args:
            val = params.get(k)
            if v.annotation == bool:
                try:
                    val = json.loads(str(val).lower())
                except json.decoder.JSONDecodeError:
                    raise ValueError(f"{k} is of type bool. Only True or False are allowed values. You provided {val}")
            if v.annotation == str:
                val = str(val)
            if v.annotation == int:
                val = int(val)
            if v.annotation == float:
                val = float(val)
            typed_params[k] = val

    args = TrainingArguments(**typed_params)

    return args
