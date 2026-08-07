from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.support_agent import ask_llm
from app.utils.session import create_conversation_id


router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None


@router.post("/chat")
async def chat(request: ChatRequest):

    print("=" * 60)
    print("INCOMING REQUEST")
    print("Message:", request.message)
    print("Conversation ID:", request.conversation_id)
    print("=" * 60)

    if request.conversation_id:
        conversation_id = request.conversation_id
        print("Using existing conversation:", conversation_id)
    else:
        conversation_id = create_conversation_id()
        print("Created new conversation:", conversation_id)

    answer = await ask_llm(
        message=request.message,
        conversation_id=conversation_id
    )

    return {
        "conversation_id": conversation_id,
        "question": request.message,
        "answer": answer
    }