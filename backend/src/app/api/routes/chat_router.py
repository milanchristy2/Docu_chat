from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from backend.src.app.schemas.schemas import MessageCreate,MessageResponse
from backend.src.app.database.session import get_db
from backend.src.app.services.chat_service import handle_chat

router=APIRouter(prefix="/chats")

@router.post("/{chat_id}/messages",response_model=MessageResponse)
def chat(chat_id:UUID,payload:MessageCreate,db:Session=Depends(get_db)):
    if payload.chat_id!=chat_id:
        raise HTTPException(status_code=400,detail="chat id mismatch")
    answer=handle_chat(
        db=db,
        chat_id=str(chat_id),
        question=payload.content,
    )
    if not answer:
        raise HTTPException(status_code=404,detail="conversation not found")
    return MessageResponse(role="assistant",content=str(answer))