from backend.src.app.utils.prompt_template import RAG_PROMPT

from langchain_community.llms import Ollama

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.runnables import RunnablePassthrough

from backend.src.app.rag.retriever import retreiver

prompt=RAG_PROMPT

def build_rag_chain():
    llm=Ollama(model="llama3.2-vision:latest")

    chain=(
        {
            "context":retreiver,
            "question":RunnablePassthrough()
        }

        | prompt
        | llm 
    )
    return chain 

