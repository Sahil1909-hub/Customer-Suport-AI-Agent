from typing import Optional
from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.support_agent import ask_llm, get_conversation_history
from app.utils.session import create_conversation_id


router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[UUID] = None


class ChatResponse(BaseModel):
    conversation_id: UUID
    question: str
    answer: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    # Use existing conversation ID
    # or create a new UUID
    if request.conversation_id:
        conversation_id = request.conversation_id
    else:
        conversation_id = UUID(create_conversation_id())

    answer = await ask_llm(
        message=request.message,
        conversation_id=str(conversation_id)
    )

    return {
        "conversation_id": conversation_id,
        "question": request.message,
        "answer": answer
    }



@router.get("/conversations/{conversation_id}")
async def get_history(conversation_id: str):

    messages = await get_conversation_history(
        conversation_id
    )

    return {
        "conversation_id": conversation_id,
        "messages": [
            {
                "role": (
                    "user"
                    if message.type == "human"
                    else "assistant"
                ),
                "content": message.content
            }
            for message in messages
        ]
    }