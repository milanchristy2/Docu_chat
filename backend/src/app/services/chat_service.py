from sqlalchemy.orm import Session
import uuid
from backend.src.app.models.db_models import Messages,Chats
from backend.src.app.rag.rag_chain import run_rag

def handle_chat(db:Session,chat_id:str,question:str,document_id:int):
    chat=db.query(Chats).filter(Chats.id==chat_id).first()
    if not chat:
        chat=Chats(
            id=uuid.UUID(chat_id),
            user_id=uuid.uuid4(),
            document_id=document_id
        )
        db.add(chat)
        db.commit()
    else:
        # Update document_id if provided and different
        if document_id and chat.document_id != document_id:
            chat.document_id = document_id
            db.commit()
    
    # Use the document_id from the current request (most up-to-date)
    result=run_rag(question=question,document_id=str(document_id))
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


