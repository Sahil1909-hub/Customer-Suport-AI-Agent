from mistralai.client import Mistral
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os
import json

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)

SYSTEM_PROMPT = """
You are an AI model router.

Choose exactly one model.

Available models:

groq
- Best for reasoning
- Coding
- Customer support
- General conversations
- Medium and complex tasks

mistral
- Fast
- Cheap
- Greetings
- FAQs
- Simple questions

nvidia
- Long explanations
- Deep analysis
- Large context
- Technical documentation

Return ONLY valid JSON.

Example:
{"model":"groq"}
"""


def router_node(state):

    latest_message = ""

    # Find the latest user message
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            latest_message = msg.content
            break

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": latest_message
            }
        ],
        temperature=0
    )

    result = json.loads(
        response.choices[0].message.content
    )

    state["model"] = result["model"]

    return state