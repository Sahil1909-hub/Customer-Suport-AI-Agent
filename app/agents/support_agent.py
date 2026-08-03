import os
from dotenv import load_dotenv
import httpx


LITELLM_URL = os.getenv(
    "LITELLM_URL",
    "http://localhost:4000/chat/completions"
)

async def ask_llm(message:str):

    payload = {
        "model": "groq",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            LITELLM_URL,
            json=payload
        )

        data =  response.json()

        return data["choices"][0]["message"]["content"]
