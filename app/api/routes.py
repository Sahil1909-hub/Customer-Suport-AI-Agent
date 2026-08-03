from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.support_agent import ask_llm

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):

    answer = await ask_llm(request.message)

    return {
        "question": request.message,
        "answer": answer
    }