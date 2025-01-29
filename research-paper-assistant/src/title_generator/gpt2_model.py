from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class TitleGenerator:
    def __init__(self, text: str):
        self.text = text
        self.model_name = "gpt2"
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)

    def generate_title(self) -> str:
        inputs = self.tokenizer.encode(self.text, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=10, num_return_sequences=1)
        title = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return title