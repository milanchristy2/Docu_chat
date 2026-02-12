from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
import uuid

from backend.src.app.database.session import get_db
from backend.src.app.services.chat_service import handle_chat
from backend.src.app.schemas.schemas import MessageCreate,MessageResponse

router=APIRouter(prefix="/query")

@router.post("/")
def query(payload:MessageCreate,db:Session=Depends(get_db)):
    answer=handle_chat(
        db=db,
        chat_id=str(payload.chat_id),
        question=payload.content
    )
    if answer is None:
        raise HTTPException(status_code=404,detail="chat not found")
    
    return MessageResponse(
        role="assistant",
        content=str(answer)
    )