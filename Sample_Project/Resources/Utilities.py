import torch
import asyncio
from browser_use import Agent
import pickle

class LocalGPTModel:
    def __init__(self, model_path):
        try:
            self.model = torch.load(model_path, weights_only=False)  # Load your model here without weights_only=False
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError, IndexError) as e:
            print(f"Error loading model: {e}")
            self.model = None

    def generate(self, prompt, max_length=300):
        if self.model:
            input_ids = self.model.tokenizer.encode(prompt, return_tensors='pt')
            output = self.model.generate(input_ids, max_length=max_length)
            return self.model.tokenizer.decode(output[0], skip_special_tokens=True)
        else:
            return "Model could not be loaded."

local_model = LocalGPTModel(model_path="C:/Users/Admin/gpt-neo/gpt-neox/megatron/model")

async def generate_robot_script(url, model):
    prompt = f"Generate a Robot Framework script for a login test on {url}."
    generated_script = model.generate(prompt)

    # Save the generated script to a file
    with open("login_test.robot", "w") as file:
        file.write(generated_script)

    # Start browser-use for additional automation if needed
    agent = Agent(task="Save and validate the generated Robot Framework script.", llm=model.model)
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    test_url = "https://www.facebook.com/login/"
    asyncio.run(generate_robot_script(test_url, local_model))