from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ai_agent import agent_workflow

router = APIRouter(prefix="/api/agent", tags=["agent"])


class AgentRequest(BaseModel):
    message: str
    context: str | None = None


@router.post("/chat")
async def chat_with_agent(payload: AgentRequest):
    if not payload.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    response = agent_workflow(payload.message, payload.context or "")
    return {"response": response}
