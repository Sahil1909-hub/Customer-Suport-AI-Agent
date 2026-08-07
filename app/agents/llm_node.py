import os
import httpx

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

LITELLM_URL = os.getenv(
    "LITELLM_URL",
    "http://localhost:4000/chat/completions"
)


def convert_messages(messages):
    """
    Convert LangChain messages into LiteLLM/OpenAI format.
    """

    converted = []

    for msg in messages:

        if isinstance(msg, HumanMessage):
            role = "user"

        elif isinstance(msg, AIMessage):
            role = "assistant"

        elif isinstance(msg, SystemMessage):
            role = "system"

        else:
            role = "user"

        converted.append(
            {
                "role": role,
                "content": msg.content
            }
        )

    return converted


def llm_node(state):

    messages = convert_messages(state["messages"])

    print("=" * 60)
    print("THREAD MESSAGES")
    for m in messages:
        print(m)
    print("=" * 60)

    payload = {
        "model": state["model"],
        "messages": messages
    }

    response = httpx.post(
        LITELLM_URL,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    answer = response.json()["choices"][0]["message"]["content"]

    return {
        "messages": [
            AIMessage(content=answer)
        ]
    }