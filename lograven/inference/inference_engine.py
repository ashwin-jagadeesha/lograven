from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class InferenceEngine:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        print(f"Loading local model: {model_name}")

        # Prefer GPU if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")

        # Load tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            torch_dtype=torch.float16 if self.device.type == "cuda" else torch.float32,
            device_map={"": self.device}
        )
        self.model.eval()

    def generate_answer(self, context: str, question: str) -> str:
        prompt = self.build_prompt(context, question)
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=True,
                top_p=0.9,
                temperature=0.7,
                pad_token_id=self.tokenizer.eos_token_id
            )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return self.extract_response(response, prompt)

    def build_prompt(self, context: str, question: str) -> str:
        return (
            f"<|system|>\n"
            f"You are a helpful assistant that answers questions from logs.\n"
            f"<|user|>\n"
            f"Logs:\n{context}\n\n"
            f"Question: {question}\n"
            f"<|assistant|>"
        )

    def extract_response(self, response: str, prompt: str) -> str:
        return response[len(prompt):].strip()
