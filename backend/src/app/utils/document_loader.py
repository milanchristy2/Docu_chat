from langchain_core.documents import Document
import os
import re
from typing import List
from langchain_community.document_loaders import PyPDFLoader,Docx2txtLoader,TextLoader

def normalize_text(text: str) -> str:
    """Clean up text by removing excessive spacing and normalizing whitespace."""
    # Replace multiple consecutive spaces with single space
    text = re.sub(r' {2,}', ' ', text)
    # Remove spaces between single characters (common in PDF extraction)
    # E.g., "K E Y   C O M P E T E N C I E S" -> "KEY COMPETENCIES"
    text = re.sub(r'(?<=[A-Z])\s+(?=[A-Z])', '', text)
    # Clean up multiple newlines
    text = re.sub(r'\n{2,}', '\n', text)
    # Remove leading/trailing whitespace from each line
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    return text.strip()

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
    
    # Normalize text in all documents
    for doc in documents:
        doc.page_content = normalize_text(doc.page_content)
    
    return documents