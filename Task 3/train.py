import warnings
import os
import pandas as pd
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from datasets import load_dataset
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForLanguageModeling, TextDataset

# Ignore warnings
#----------------
os.environ["WANDB_DISABLED"] = "true"
warnings.filterwarnings("ignore")

device = 'cuda' if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else 'cpu')

os.system('cls' if os.name == 'nt' else 'clear')
print("Your device is: " + device)

# Load base model
#----------------
model_name_or_path = 'ai-forever/rugpt3small_based_on_gpt2'

tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)

model = GPT2LMHeadModel.from_pretrained(model_name_or_path).to(device) # type: ignore

# Fine-tuning base model
#----------------
dataset = load_dataset(
     "mlsum", "ru", 
     split="train")


filtered_dataset = dataset.filter(lambda example: example['topic'] == 'economics')

pandas_data = pd.DataFrame(filtered_dataset['text']) # type: ignore

text_column = pandas_data[0]

output_file_path = 'Task 3/output.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for example in text_column:
        output_file.write(example)


train_dataset = TextDataset(tokenizer=tokenizer, file_path='Task 3/output.txt', 
                            block_size=64)
  
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, 
                                                mlm=False)


training_args = TrainingArguments(
    output_dir = "Task 3/finetuned_model",
    overwrite_output_dir = True,
    num_train_epochs = 5,
    gradient_accumulation_steps = 2,
    fp16 = True,
    per_device_train_batch_size = 16,
    learning_rate = 0.0002,
    optim = 'adafactor',
    lr_scheduler_type = 'cosine'
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator
)

trainer.train()

trainer.save_model("Task 3/finetuned_model")