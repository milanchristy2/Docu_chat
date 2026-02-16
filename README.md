# DocuChat - RAG-Based Question Answering System

A Retrieval-Augmented Generation (RAG) system that enables users to upload documents (PDF or text files) and interact with them conversationally using a Large Language Model (LLM).

---

## Features

- 📄 **Document Upload** - Upload PDF or text files
- 💬 **Conversational QA** - Chat with your documents using natural language
- 🔍 **Semantic Search** - Retrieve relevant document chunks using embeddings
- 🧠 **AI-Powered Answers** - Generate context-aware responses using LLM
- 📊 **Evaluation Metrics** - Track faithfulness, answer relevancy, context precision, and recall
- 🗄️ **Chat History** - Persistent conversation storage

---

## Technology Stack

### Backend
- **Framework**: FastAPI
- **Database**: SQLAlchemy ORM with SQLite/PostgreSQL
- **Migrations**: Alembic
- **AI/LLM**: LangChain, Ollama (llama3.2-vision:latest)
- **Embeddings**: Ollama (mxbai-embed-large)
- **Vector Store**: FAISS / ChromaDB

### Frontend
- **Framework**: React 19
- **Build Tool**: Vite
- **Styling**: Bootstrap 5
- **HTTP Client**: Axios

---

## Prerequisites

Before running the project, ensure you have:

1. **Python 3.10+** installed
2. **Node.js 18+** installed
3. **Ollama** installed and running locally

### Install Ollama

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama service
ollama serve

# Pull required models (in a new terminal)
ollama pull llama3.2-vision:latest
ollama pull mxbai-embed-large
```

---

## Project Setup

### 1. Clone the Repository

```bash
cd /Users/milanchristy/Desktop/Docu_chat
```

### 2. Backend Setup

#### Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

#### Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### Environment Configuration

Create a `.env` file in the project root:

```env
# Database (use SQLite for development, PostgreSQL for production)
DATABASE_URL=sqlite:///./rag.db

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
LLAMA_MODEL=llama3.2-vision:latest
EMBEDDING_MODEL=mxbai-embed-large

# Vector Store Configuration
VECTOR_STORE_TYPE=faiss  # or chromadb
```

#### Run Database Migrations

```bash
cd /Users/milanchristy/Desktop/Docu_chat
alembic upgrade head
```

#### Start the Backend Server

```bash
# From project root
python -m backend.src.app.main
```

The backend will run at: **http://localhost:8000**

---

### 3. Frontend Setup

#### Navigate to Frontend Directory

```bash
cd /Users/milanchristy/Desktop/Docu_chat/frontend
```

#### Install Dependencies

```bash
npm install
```

#### Start the Frontend Development Server

```bash
npm run dev
```

The frontend will run at: **http://localhost:5173**

---

## Running the Application

### Option 1: Development Mode

1. **Start Ollama** (in a terminal):
   ```bash
   ollama serve
   ```

2. **Start Backend** (in a new terminal):
   ```bash
   cd /Users/milanchristy/Desktop/Docu_chat
   source venv/bin/activate
   python -m backend.src.app.main
   ```

3. **Start Frontend** (in another terminal):
   ```bash
   cd /Users/milanchristy/Desktop/Docu_chat/frontend
   npm run dev
   ```

4. Open browser: **http://localhost:5173**

### Option 2: Production Build

```bash
# Build frontend
cd /Users/milanchristy/Desktop/Docu_chat/frontend
npm run build

# Serve the build (using any static file server)
npm run preview
```

---

## API Endpoints

### Document Upload
```
POST /documents/upload/
Content-Type: multipart/form-data
Body: file (PDF or text file)
```

### Query/Chat
```
POST /query/
Content-Type: application/json
Body: {
  "chat_id": "uuid-string",
  "content": "Your question here"
}
```

### Create New Chat
```
POST /chats/
Content-Type: application/json
Body: {
  "user_id": "user-identifier"
}
```

### Get Chat History
```
GET /chats/{chat_id}/messages
```

---

## Project Structure

```
Docu_chat/
├── backend/
│   └── src/
│       └── app/
│           ├── api/
│           │   └── routes/
│           │       ├── chat_router.py
│           │       ├── query_router.py
│           │       └── upload_router.py
│           ├── core/
│           │   └── config.py
│           ├── database/
│           │   └── session.py
│           ├── models/
│           │   └── db_models.py
│           ├── rag/
│           │   ├── ingest_documents.py
│           │   ├── rag_chain.py
│           │   └── retriever.py
│           ├── schemas/
│           │   └── schemas.py
│           ├── services/
│           │   ├── chat_service.py
│           │   ├── document_service.py
│           │   └── evaluation_service.py
│           └── utils/
│               ├── document_loader.py
│               ├── prompt_template.py
│               └── text_splitter.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat.jsx
│   │   │   ├── Navbar.jsx
│   │   │   └── Upload.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── alembic/
│   └── versions/
├── docs/
│   └── docu_chat-design.md
├── requirements.txt
└── README.md
```

---

### Vector Store

Set in `.env`:
```env
VECTOR_STORE_TYPE=faiss  # or chromadb
```

### LLM Model

Set in `.env`:
```env
LLAMA_MODEL=llama3.2-vision:latest
```

---

## Troubleshooting

### Issue: Ollama not running
```bash
# Check if Ollama is running
ollama list

# If not, start it
ollama serve
```

### Issue: Database connection error
```bash
# Check DATABASE_URL in .env
# For SQLite, ensure the file path is correct

# Run migrations
alembic upgrade head
```

### Issue: Frontend can't connect to backend
- Ensure backend is running on http://localhost:8000
- Check CORS settings in `backend/src/app/main.py`
- Verify frontend API base URL in `frontend/src/services/api.js`

### Issue: Vector store errors
- Delete existing vector store: `backend/src/app/data/vector_store/`
- Re-upload documents to rebuild index

---

## Development Notes

- Files are stored locally in `backend/src/app/data/`
- Vector store is in `backend/src/app/data/vector_store/`
- Database is at `backend/src/app/database/rag.db`
- Use Alembic for database migrations: `alembic revision --autogenerate`

---


