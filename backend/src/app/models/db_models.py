from sqlalchemy import Column,Text,String,UUID,DateTime,ForeignKey
from sqlalchemy.orm import relationship,Mapped,mapped_column
from backend.src.app.core.config import Base
import uuid,datetime

class Document(Base):
    __tablename__="documents"
    id:Mapped[int]=mapped_column(primary_key=True,index=True,nullable=False)
    filename:Mapped[str]=mapped_column(String,index=True)
    content_text:Mapped[str]=mapped_column(Text)
    uploaded_at:Mapped[datetime.datetime]=mapped_column(DateTime,default=datetime.datetime.utcnow,index=True)

class Chats(Base):
    __tablename__="chats"
    id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    user_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),nullable=False,index=True)
    messages:Mapped[list["Messages"]]=relationship("Messages",back_populates="chats",cascade="all, delete-orphan")

class Messages(Base):
    __tablename__="messages"
    id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    chat_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),ForeignKey("chats.id"),index=True,nullable=False)
    role:Mapped[str]=mapped_column(String)
    content:Mapped[str]=mapped_column(Text)
    chats=relationship("Chats",back_populates="messages")
    evaluation:Mapped["Evaluation"]=relationship("Evaluation",back_populates="message",uselist=False,cascade="all,delete-orphan")

class Evaluation(Base):
    __tablename__="evaluations"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    message_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),ForeignKey("messages.id",ondelete="CASCADE"),nullable=False,index=True)
    faithfulness:Mapped[float]=mapped_column(nullable=True)
    answer_relevancy:Mapped[float]=mapped_column(nullable=True)
    context_precision:Mapped[float]=mapped_column(nullable=True)
    context_recall:Mapped[float]=mapped_column(nullable=True)
    created_at:Mapped[datetime.datetime]=mapped_column(DateTime,default=datetime.datetime.utcnow)
    message:Mapped["Messages"]=relationship("Messages",back_populates="evaluation")