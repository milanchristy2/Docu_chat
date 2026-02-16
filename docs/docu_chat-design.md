# DocuChat – System Design Document
A Retrieval-Augmented Generation (RAG) Based Question Answering System

---

# 1. Introduction

DocuChat is an end-to-end Retrieval-Augmented Generation (RAG) system that enables users to upload documents (PDF or text files) and interact with them conversationally using a Large Language Model (LLM).

Instead of relying solely on the model’s pre-trained knowledge, DocuChat retrieves relevant document chunks from a vector database and injects them into the LLM prompt to generate grounded, context-aware responses.

This architecture ensures higher factual accuracy, domain specificity, and reduced hallucination.

---

# 2. System Overview

## 2.1 High-Level Flow

1. User uploads document(s)
2. Document is stored locally
3. Text is extracted
4. Document is split into chunks
5. Chunks are embedded using an embedding model
6. Embeddings are stored in a vector database
7. User submits a query
8. Top-k relevant chunks are retrieved
9. LLM generates a response using retrieved context
10. Response is stored in PostgreSQL
11. Evaluation runs asynchronously

---

## 2.2 Architecture Diagram (Conceptual)

Frontend (React + Bootstrap)
        ↓
FastAPI Backend
        ↓
RAG Pipeline
   ↙            ↘
Vector Store     LLM (Ollama)
        ↓
PostgreSQL
        ↓
Background Evaluation Service

---

# 3. Technology Stack

## Backend
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Alembic (database migrations)

## AI Layer
- LLM: Ollama (llama3.2-vision:latest)
- Embeddings: Ollama (mxbai-embed-large)
- Vector Store: FAISS or ChromaDB
- LangChain (pipeline orchestration)

## Frontend
- React
- Bootstrap (utility-first CSS)
- Google Fonts

---

# 4. Database Design

## 4.1 Tables

### Documents
- id (Primary Key)
- filename
- content_text
- uploaded_at

### Chats
- id (Primary Key)
- user_id

### Messages
- id (Primary Key)
- chat_id (Foreign Key)
- role (user / assistant)
- content

### Evaluations
- id (Primary Key)
- message_id (Foreign Key)
- faithfulness
- answer_relevancy
- context_precision
- context_recall

---

## 4.2 Relationships

- One Chat → Many Messages (One-to-Many)
- One Message → One Evaluation (One-to-One)
- Documents → Chunked and stored in Vector Database

---

# 5. RAG Pipeline

## 5.1 Document Ingestion

Steps:
1. Load document
2. Extract raw text
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in vector store

---

## 5.2 Chunking Strategy

Recommended configuration:

chunk_size = 800  
chunk_overlap = 150  
separators = ["\n\n", "\n", ".", " ", ""]

Alternative configurations:

For dense/legal documents:
chunk_size = 600  
chunk_overlap = 150  

For books:
chunk_size = 1000  
chunk_overlap = 200  

Chunk size significantly affects:
- Retrieval quality
- Embedding efficiency
- Context relevance


# 6. Evaluation Pipeline

Evaluation runs asynchronously to prevent blocking API responses.

Metrics calculated:
- Faithfulness
- Answer Relevancy
- Context Precision
- Context Recall

Evaluation Service:
- Independent database session
- Background execution
- Results stored in Evaluations table

Evaluation is CPU-intensive depending on document size and context length.

---

# 7. Challenges Faced

1. Integrating evaluation within RAG pipeline
2. Managing embedding context limits
3. Handling large file ingestion
4. Optimizing OS-level CPU and memory usage
5. Designing relational schema for conversations
6. Implementing async background tasks

---

# 8. Security & Limitations

- Files stored locally (not production-ready)
- No authentication system
- No distributed task queue
- Evaluation is CPU-heavy
- Limited horizontal scalability

---

# 9. Learning Outcomes

- Built a full-stack RAG system
- Designed database schema for conversational AI
- Integrated vector database with LLM
- Implemented async evaluation
- Optimized ingestion using batching
- Understood system-level performance tuning

---


---

# Conclusion

DocuChat demonstrates a complete Retrieval-Augmented Generation system integrating:

- Document ingestion
- Semantic retrieval
- LLM-based response generation
- Database persistence
- Evaluation metrics

It serves as a practical implementation of modern AI system architecture.
