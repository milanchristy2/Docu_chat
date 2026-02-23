from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List

class ChatCreate(BaseModel):
    user_id:UUID

class ChatResponse(BaseModel):
    id:UUID

class MessageCreate(BaseModel):
    chat_id:UUID
    content:str
    document_id:int 

class MessageResponse(BaseModel):
    role:str
    content:str

class EvidenceItem(BaseModel):
    source: str
    text: str

class RagMessageResponse(BaseModel):
    role: str
    answer: str
    explanation: Optional[str] = ""
    evidence: List[EvidenceItem] = []
    follow_up: Optional[str] = ""
    confidence: float = 0.0
    contexts: List[str] = []

class DocumentUpload(BaseModel):
    document_id:int