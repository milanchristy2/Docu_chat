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