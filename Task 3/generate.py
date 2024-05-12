import warnings
import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

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

BASE_PROMT = "Увы, эксперты уверены —" # Введите свой промт
MAX_LENGTH = 100 # Укажите предельную длину генерации

def generate(prompt, do_sample=True, num_beams=2, temperature=1.5, top_p=0.9, max_length=MAX_LENGTH):
    
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    model.eval()
    with torch.no_grad():
        out = model.generate(input_ids, 
                            do_sample=do_sample,
                            num_beams=num_beams,
                            temperature=temperature,
                            top_p=top_p,
                            max_length=max_length,
                            )
        
    decoded_out = list(map(lambda x: tokenizer.decode(x, skip_special_tokens=True), out))
    
    truncated_output = []
    for text in decoded_out:
        if len(text) > max_length:
            last_dot_index = max(text.rfind('.'), text.rfind('!'), text.rfind('?'))
            if last_dot_index != -1:
                truncated_output.append(text[:last_dot_index + 1])
            else:
                truncated_output.append(text[:max_length])
        else:
            truncated_output.append(text)
    
    return truncated_output

base_result = generate(BASE_PROMT)

# Load fine-tuninged base model
#----------------
model_path = "Task 3/finetuned_model"
model = GPT2LMHeadModel.from_pretrained(model_path).to(device) # type: ignore

new_result = generate(BASE_PROMT)

os.system('cls' if os.name == 'nt' else 'clear')

print('\n Результаты генерации \n')
print(f'Базовая модель: \n\n{base_result}')
print()
print(f'Дообученная модель: \n\n{new_result}')