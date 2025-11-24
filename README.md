Below is a **clean, professional, and industry-standard README.md** tailored for your **Past Question RAG Bot** project.
It includes installation, usage, folder structure, environment setup, and API endpoints—perfect for GitHub.

Let me know if you want to add **badges, images, a logo, or a demo video section**.

---

# ✅ **README.md (Professional Version)**

```
# 📚 Past Question RAG Bot  
An AI-powered Retrieval-Augmented Generation (RAG) system that allows students to search, summarize, and query academic past questions using modern LLMs, embeddings, and vector search.

This system uses:
- 🧠 Large Language Models (LLMs)
- 🔍 Document Embeddings
- 📦 ChromaDB Vector Store
- 📄 PDF ingestion + text splitting
- ⚡ FastAPI backend

---

## 🚀 Features
- Upload multiple PDF past questions.
- Automatic text extraction and chunking.
- Embedding generation using SentenceTransformers.
- ChromaDB vector store for efficient retrieval.
- Query answering using RAG (retrieval + LLM).
- Clean modular architecture for production.

---

## 📁 Project Structure

```

past-question-rag-bot/
│

├── data/

│   └── pdfs/                # Raw PDF documents

│

├── vectorstore/             # ChromaDB/Faiss database

│

├── src/

│   ├── **init**.py

│   ├── config.py            # Environment variables loader

│   ├── embeddings.py        # Embedding model setup

│   ├── loader.py            # PDF loading + text splitting

│   ├── vectorstore.py       # Vector DB creation and search

│   ├── rag_pipeline.py      # RAG chain construction

│   └── app.py               # FastAPI app server

│

├── .env                     # Environment variables (ignored by Git)

├── .env.example             # Safe template to share

├── .gitignore               # Files to ignore

├── requirements.txt         # Python dependencies

└── README.md                # Documentation

````

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the repository
```powershell
git clone https://github.com/olamide421/past-question-rag-bot.git
cd past-question-rag-bot
````

### 2️⃣ Create virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```powershell
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file

```
USE_OPENAI=true
OPENAI_API_KEY=your_api_key_here
LLM_MODEL=gpt-4o-mini
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
VECTOR_STORE_DIR=vectorstore/chroma_db
HOST=127.0.0.1
PORT=8000
DATA_DIR=data/pdfs
```

Or duplicate the example file:

```powershell
cp .env.example .env
```

---

## 📥 Add Your PDF Files

Place all your past question PDFs into:

```
data/pdfs/
```

You can add multiple PDF files — the app will automatically process them.

---

## ▶️ Run the Pipeline (Build embeddings + VectorDB)

```powershell
python -m src.rag_pipeline
```

This step will:

* Load all PDFs
* Split text into chunks
* Encode with embeddings
* Save to vector store

---

## 🌐 Run the API Server

```powershell
python -m src.app
```

Server starts at:

```
http://127.0.0.1:8000
```

Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 API Endpoints

### **POST /ask**

Ask any question about the PDF documents.

**Request:**

```json
{
  "query": "Explain the principle of heat conduction."
}
```

**Response:**

```json
{
  "answer": "Heat conduction is the process..."
}
```

---

## 🏗️ Tech Stack

* **Python 3.10+**
* **LangChain**
* **ChromaDB**
* **SentenceTransformers**
* **FastAPI**
* **Uvicorn**
* **PyPDFLoader**

---

## 🙌 Contributing

Contributions are welcome.
Feel free to open issues or submit PRs.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Future Enhancements

* Web UI for uploading PDFs
* Support for audio lecture retrieval
* Local LLM using Llama, Gemma, or Mistral
* Vector index auto-refresh

---

## ⭐ Like this project?


Just tell me what you want!
```
