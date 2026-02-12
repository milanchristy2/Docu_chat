from sqlalchemy.orm import Session
from backend.src.app.models.db_models import Document as DBDocument
from backend.src.app.utils.documents_storage import save_docs
from backend.src.app.utils.document_loader import load_document
from backend.src.app.utils.text_splitter import split_docs
from backend.src.app.rag.retriever import vectorstore
from backend.src.app.rag.ingest_documents import ingest_docs

def upload_documents(db:Session,filename:str,file_bytes:bytes)->int:
    file_path=save_docs(filename,file_bytes)
    documents=load_document(file_path)
    full_txt=""
    for doc in documents:
        full_txt+=doc.page_content+"\n"


    db_doc=DBDocument(filename=filename,content_text=full_txt)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)

    chunks=split_docs(documents)
    ingest_docs(chunks,document_id=str(db_doc.id))

    return db_doc.id
