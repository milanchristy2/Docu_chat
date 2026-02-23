from backend.src.app.utils.prompt_template import RAG_PROMPT
from langchain_community.llms import Ollama
from backend.src.app.rag.retriever import vectorstore
import re
import json
import logging

LLM = Ollama(model="llama3.2-vision:latest", temperature=0.0)

def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()

def _extract_json_from_text(text: str) -> dict:
    """Extract and parse JSON from text, with fallback."""
    text = str(text).strip()
    
    # Try direct JSON parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    # Try extracting JSON between first { and last }
    try:
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1 and start < end:
            json_str = text[start:end+1]
            return json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        pass
    
    # Return default if all parsing fails
    return {
        "answer": text,
        "explanation": "",
        "evidence": [],
        "follow_up": "",
        "confidence": 0.0
    }

def run_rag(question: str, document_id: str):
    """Run RAG pipeline: retrieve documents, build context, query LLM, parse response."""
    
    # Retrieve relevant documents
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 6, "filter": {"document_id": {"$eq": document_id}}}
    )
    retrieved_docs = retriever.invoke(question)
    
    # Fallback if no docs found with filter
    if not retrieved_docs:
        logging.warning(f"No docs found for document_id {document_id}. Trying without filter.")
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
        retrieved_docs = retriever.invoke(question)
    
    # Build numbered context from documents
    context_parts = []
    for idx, doc in enumerate(retrieved_docs, start=1):
        content = clean_text(doc.page_content)
        source_id = doc.metadata.get("source", f"doc_{idx}") if doc.metadata else f"doc_{idx}"
        context_parts.append(f"[{idx}] {source_id}:\n{content}")
    
    context = "\n\n".join(context_parts)
    
    # Build and invoke RAG chain
    chain = RAG_PROMPT | LLM
    response_text = chain.invoke({"context": context, "question": question})
    
    # Parse response
    result = _extract_json_from_text(response_text)
    
    return {
        "answer": result.get("answer", ""),
        "explanation": result.get("explanation", ""),
        "evidence": result.get("evidence", []),
        "follow_up": result.get("follow_up", ""),
        "confidence": result.get("confidence", 0.0)
    }

