from langchain_core.messages import HumanMessage

from app.agents.graph import graph


async def ask_llm(message: str, conversation_id: str):

    config = {
        "configurable": {
            "thread_id": conversation_id
        }
    }

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=message)
            ]
        },
        config=config
    )

    answer = result["messages"][-1].content

    return answer


async def get_conversation_history(conversation_id: str):

    config = {
        "configurable": {
            "thread_id": conversation_id
        }
    }

    state = graph.get_state(config)

    return state.values.get("messages", [])