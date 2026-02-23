from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs(document:list):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=150,
        separators=["\n\n","\n","."," ",""]
    )

    return splitter.split_documents(document)