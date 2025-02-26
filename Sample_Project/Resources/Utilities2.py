from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import asyncio

class LocalGPTModel:
    def __init__(self, model_path):
        try:
            self.model = AutoModelForCausalLM.from_pretrained(
                model_path,
                torch_dtype=torch.float16,  # Change to torch.float32 if GPU not available
                device_map="auto",  # Moves model to GPU if available
                trust_remote_code=True  # ✅ Required to load DeepSeek-V3
            )
            self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)  # ✅ Add here too
        except Exception as e:
            print(f"Error loading model or tokenizer: {e}")
            self.model = None
            self.tokenizer = None

    def generate(self, prompt, max_length=300):
        if self.model and self.tokenizer:
            input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.model.device)
            output = self.model.generate(input_ids, max_length=max_length, num_return_sequences=1)
            return self.tokenizer.decode(output[0], skip_special_tokens=True)
        else:
            return "Model could not be loaded."

local_model = LocalGPTModel(model_path="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B")

async def generate_robot_script(url, model):
    prompt = f"Generate a Robot Framework script for a login test on {url}."
    generated_script = model.generate(prompt)

    # Save the generated script to a file
    with open("login_test.robot", "w") as file:
        file.write(generated_script)

    print("Generated script saved to login_test.robot")

if __name__ == "__main__":
    test_url = "https://www.facebook.com/login/"
    asyncio.run(generate_robot_script(test_url, local_model))
