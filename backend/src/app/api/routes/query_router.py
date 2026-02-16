from fastapi import APIRouter,Depends,HTTPException,BackgroundTasks
from sqlalchemy.orm import Session
import uuid
from backend.src.app.services.evaluation_service import run_evaluation
from backend.src.app.database.session import get_db
from backend.src.app.services.chat_service import handle_chat
from backend.src.app.schemas.schemas import MessageCreate,MessageResponse

router=APIRouter(prefix="/query")

@router.post("/")
def query(payload:MessageCreate,background_tasks:BackgroundTasks,db:Session=Depends(get_db)):
    result,message_id=handle_chat(
        db=db,
        chat_id=str(payload.chat_id),
        question=payload.content
    )
    background_tasks.add_task(
        run_evaluation,
        message_id,
        payload.content,
        result["answer"],
        result["contexts"]
    )
    if result is None:
        raise HTTPException(status_code=404,detail="chat not found")
    
    return MessageResponse(
        role="assistant",
        content=result["answer"]
    )