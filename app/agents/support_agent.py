import os
from dotenv import load_dotenv
import httpx
from app.agents.classifier import choose_model


LITELLM_URL = os.getenv(
    "LITELLM_URL",
    "http://localhost:4000/chat/completions"
)


async def ask_llm(message:str):

    model = choose_model(message)
    print(f"Selected model: {model}")

    payload = {
        "model": model,
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

        return data
