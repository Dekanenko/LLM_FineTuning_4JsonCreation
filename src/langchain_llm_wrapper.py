from langchain.llms.base import LLM
from typing import Any, List, Optional, Mapping
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class LlamaLLM(LLM):
    model: Any
    tokenizer: Any
    # device: str = "cuda" if torch.cuda.is_available() else "cpu"
    # Use MPS if available (Apple Silicon), CPU as fallback
    device: str = "mps" if torch.backends.mps.is_available() else "cpu"
    
    def __init__(self, model_name: str):
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        inputs = self.tokenizer(
            prompt,
            max_length=256,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        ).to(self.device)
        
        # Generate response
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=512,  # Adjust as needed
                temperature=0.7,  # Adjust temperature
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        # Decode and return the response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Remove the prompt from the response
        response = response[len(prompt):]
        return response.strip()
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name": "LlamaLLM"}
    
    @property
    def _llm_type(self) -> str:
        return "custom"