from pydantic import BaseModel
from uuid import UUID

class ChatCreate(BaseModel):
    user_id:UUID

class ChatResponse(BaseModel):
    id:UUID

class MessageCreate(BaseModel):
    chat_id:UUID
    content:str

class MessageResponse(BaseModel):
    role:str
    content:str

class DocumentUpload(BaseModel):
    document_id:int