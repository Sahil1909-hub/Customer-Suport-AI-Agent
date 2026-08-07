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

    # The last message in the state is the AI response
    answer = result["messages"][-1].content

    return answer