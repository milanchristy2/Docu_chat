from sqlalchemy.orm import Session
from backend.src.app.models.db_models import Messages
from backend.src.app.rag.rag_chain import build_rag_chain

def handle_chat(db:Session,chat_id:str,question:str):
    chain=build_rag_chain()
    ans=chain.invoke(question)
    db.add(
        Messages(
            chat_id=chat_id,
            role="user",
            content=question
        )
    )
    db.add(
        Messages(
            chat_id=chat_id,
            role="assistant",
            content=str(ans),
        )
    )
    db.commit()

    return ans

