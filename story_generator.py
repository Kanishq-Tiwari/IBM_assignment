from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class StoryGenerator:
    def __init__(self, model_name="gpt2-medium"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()

    def generate_story(self, prompt, max_length=300):
        input_ids = self.tokenizer(prompt, return_tensors="pt", truncation=True).input_ids
        with torch.no_grad():
            output = self.model.generate(
                input_ids,
                max_length=max_length,
                temperature=0.9,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                pad_token_id=self.tokenizer.eos_token_id
            )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
