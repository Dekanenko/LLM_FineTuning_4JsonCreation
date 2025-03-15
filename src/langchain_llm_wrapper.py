from langchain.llms.base import LLM
from typing import Any, List, Optional, Mapping
import torch
from pydantic import Field
from src.utils import generate_prompt


class LlamaLLM(LLM):
    model: Any = Field(default=None)
    tokenizer: Any = Field(default=None)
    device: str = Field(default="cuda" if torch.cuda.is_available() else "cpu")
    max_new_tokens: int = Field(default=1024)
    # Use MPS if available (Apple Silicon), CPU as fallback
    # device: str = Field(default="mps" if torch.backends.mps.is_available() else "cpu")

    def __init__(self, model, tokenizer, max_new_tokens=1024):
        super().__init__()
        self.tokenizer = tokenizer
        self.model = model
        self.max_new_tokens = max_new_tokens

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any
    ) -> str:

        prompt = generate_prompt({"input": prompt}, train=False)
        inputs = self.tokenizer(prompt, padding=True, return_tensors="pt").to("cuda")

        # Generate response
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_new_tokens=self.max_new_tokens,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )

        # Decode and return the response
        response = self.tokenizer.decode(outputs[0])
        separator = "<|start_header_id|>assistant<|end_header_id|>"

        # Split and take everything after the separator
        response = response.split(separator, 1)[-1].replace("<|eot_id|>", "")
        return response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name": "LlamaLLM"}

    @property
    def _llm_type(self) -> str:
        return "custom"
