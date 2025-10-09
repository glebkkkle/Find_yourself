
from trl import SFTTrainer
from datasets import load_dataset


from unsloth import FastModel
import torch

from trl import LoraConfig

max_seq_length = 2048


model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/mistral",
    max_seq_length = max_seq_length, 
    load_in_4bit = True,  
    load_in_8bit = False, 
    full_finetuning = False,

)

model = FastModel.get_peft_model(
    model,
    r = 128,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 128,
    lora_dropout = 0,
    bias = "none",    

    use_gradient_checkpointing = "unsloth", 
    random_state = 3407,
    use_rslora = False, 
    loftq_config = LoraConfig, # And LoftQ
)

from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma3",
)

from datasets import load_dataset
dataset = load_dataset("glebkle/projj", split = "train[:10000]")


def convert_to_chatml(example):
    return {
        "conversations": [
            {"role": "system", "content": example["task"]},
            {"role": "user", "content": example["input"]},
            {"role": "assistant", "content": example["expected_output"]}
        ]
    }

dataset = dataset.map(
    convert_to_chatml
)


def formatting_prompts_func(examples):
   convos = examples["conversations"]
   texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False).removeprefix('<bos>') for convo in convos]
   return { "text" : texts, }

dataset = dataset.map(formatting_prompts_func, batched = True)


from trl import SFTTrainer, SFTConfig
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    eval_dataset = None, 
    args = SFTConfig(
        dataset_text_field = "text",
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 1, 
        warmup_steps = 5,

        max_steps = 100,
        learning_rate = 5e-5, 
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir="outputs",
        report_to = "none", 
    ),
)


from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<start_of_turn>user\n",
    response_part = "<start_of_turn>model\n",
)



trainer_stats = trainer.train()


messages = [
    {'role': 'system','content':dataset['conversations'][10][0]['content']},
    {"role" : 'user', 'content' : dataset['conversations'][10][1]['content']}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True,
).removeprefix('<bos>')

from transformers import TextStreamer

_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 125,
    temperature = 1, top_p = 0.95, top_k = 64,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)

