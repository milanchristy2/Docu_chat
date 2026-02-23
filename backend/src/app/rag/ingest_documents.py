from backend.src.app.rag.retriever import vectorstore
import logging

def ingest_docs(documents,document_id:str):
    """Add documents to vectorstore with document_id metadata."""
    logging.info(f"Ingesting {len(documents)} chunks with document_id={document_id}")
    
    for doc in documents:
        doc.metadata["document_id"]=str(document_id)
    
    result = vectorstore.add_documents(documents)
    logging.info(f"Successfully added {len(documents)} documents to vectorstore. IDs: {result}")