from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key= os.getenv('OPENROUTER_API_KEY'),
    base_url="https://openrouter.ai/api/v1",
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {"role": "user", "content": "My name is Sahil!"}
    ]
)


print(response.choices[0].message.content)