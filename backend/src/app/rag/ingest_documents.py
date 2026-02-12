from backend.src.app.rag.retriever import vectorstore

def ingest_docs(documents,document_id:str):
    for doc in documents:
        doc.metadata["document_id"]=document_id

    vectorstore.add_documents(documents)