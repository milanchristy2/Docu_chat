from fastapi import Depends,APIRouter,HTTPException,UploadFile
from sqlalchemy.orm import Session

from backend.src.app.schemas.schemas import DocumentUpload
from backend.src.app.database.session import get_db
from backend.src.app.services.document_service import upload_documents

router=APIRouter(prefix="/documents")

@router.post("/upload",response_model=DocumentUpload)
async def upload_docs(file:UploadFile,db:Session=Depends(get_db)):
    if not file.filename:
        raise HTTPException(status_code=400,detail="filename is required")
    file_bytes=await file.read()
    docs_id=upload_documents(
        db=db,
        filename=file.filename,
        file_bytes=file_bytes
    )
    return DocumentUpload(document_id=docs_id)