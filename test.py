import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv() 

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN not set in environment variables")

client = InferenceClient(api_key=HF_TOKEN)

def get_ai_response(prompt):
    completion = client.chat.completions.create(
        model="facebook/blenderbot-400M-distill",  # a supported chat model
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    response = get_ai_response("Hello, what can you do?")
    print(response)
