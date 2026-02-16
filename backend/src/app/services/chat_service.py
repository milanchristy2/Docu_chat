from sqlalchemy.orm import Session
import uuid
from backend.src.app.models.db_models import Messages,Chats
from backend.src.app.rag.rag_chain import run_rag

def handle_chat(db:Session,chat_id:str,question:str):
    chat=db.query(Chats).filter(Chats.id==chat_id).first()
    if not chat:
        chat=Chats(
            id=uuid.UUID(chat_id),
            user_id=uuid.uuid4()
        )
        db.add(chat)
        db.commit()
    result=run_rag(question=question)
    answer=result['answer']
    user_message=Messages(
            chat_id=chat.id,
            role="user",
            content=question
        )
    db.add(user_message)
    assistant_message=Messages(
            chat_id=chat.id,
            role="assistant",
            content=answer,
        )
    db.add(assistant_message)
    db.commit()
    db.refresh(assistant_message)

    return result,assistant_message.id


