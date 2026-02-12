from langchain_core.documents import Document
import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader,Docx2txtLoader,TextLoader
def load_document(filepath:str)->List[Document]:
    _,ext=os.path.splitext(filepath)
    ext=ext.lower()
    if ext==".pdf":
        loader=PyPDFLoader(filepath)
    elif ext==".docx":
        loader=Docx2txtLoader(filepath)
    elif ext==".txt":
        loader=TextLoader(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    documents=loader.load()
    return documents