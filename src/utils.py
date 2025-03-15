def generate_prompt(data_sample, train=True):
    prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{data_sample["input"]}<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>
"""
    if train:
        prompt += f"{data_sample['output']}<|eot_id|>"
    return prompt.strip()


def generate_and_tokenize_prompt(data_sample, tokenizer, max_length=2048):
    prompt = generate_prompt(data_sample)
    tokenized_prompt = tokenizer(
        prompt,
        max_length=max_length,
        padding="max_length",
        truncation=True,
    )
    return tokenized_prompt
