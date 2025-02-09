import torch
from torch.utils.data import Dataset
import json
from transformers import AutoTokenizer

class JsonDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length=1024):
        self.tokenizer = tokenizer
        self.max_length = max_length
        
        self.tokenized_data = []
        
        with open(file_path, 'r') as f:
            for line in f:
                item = json.loads(line)
                
                input_tokens = self.tokenizer(
                    item['input'],
                    max_length=self.max_length,
                    padding='max_length',
                    truncation=True,
                    return_tensors='pt'
                )
                
                output_tokens = self.tokenizer(
                    item['output'],
                    max_length=self.max_length,
                    padding='max_length',
                    truncation=True,
                    return_tensors='pt'
                )
                
                self.tokenized_data.append({
                    'input_ids': input_tokens['input_ids'].squeeze(0),
                    'attention_mask': input_tokens['attention_mask'].squeeze(0),
                    'labels': output_tokens['input_ids'].squeeze(0)
                })
    
    def __len__(self):
        return len(self.tokenized_data)
    
    def __getitem__(self, idx):
        return self.tokenized_data[idx]