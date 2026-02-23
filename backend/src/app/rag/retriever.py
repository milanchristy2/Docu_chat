from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings 
from pathlib import Path

CHROMA_PATH=Path.cwd()/"chroma_db"
CHROMA_PATH.mkdir(parents=True,exist_ok=True)
embeddings=OllamaEmbeddings(model="mxbai-embed-large")

vectorstore=Chroma(
    persist_directory=str(CHROMA_PATH),
    embedding_function=embeddings
)

# retreiver=vectorstore.as_retriever(search_type="mmr",search_kwargs={"k":3,"fetch_k":10})


