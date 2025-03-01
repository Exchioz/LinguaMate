import asyncio
from fastapi import APIRouter, Request
from .models import ChatRequest
from .generate import generate_response, evaluate_conversation
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.post("/chat")
@limiter.limit("10/minute")
async def chat(request: Request, request_data: ChatRequest):
    ai_response = await asyncio.to_thread(generate_response, request_data.message, request_data.difficulty, request_data.style)
    evaluation = None
    if request_data.evaluate:
        evaluation = await asyncio.to_thread(evaluate_conversation, request_data.message, ai_response)
    
    return {"response": ai_response, "evaluation": evaluation}

@router.get("/health")
async def health_check():
    return {"status": "OK"}
