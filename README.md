# RAG PDF Chatbot (Work in Progress) 📄

An AI-powered research assistant that allows users to upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG).

---

## 🎯 Project Goal

Build a system where:
- Users upload one or more PDF files (e.g. research papers)
- The system reads and indexes the documents
- Users can ask natural-language questions
- The system answers using the content of the uploaded PDFs
- Answers include references to the source documents

This is a common real-world pattern used in enterprise AI systems.

---

## 🧠 What This Project Will Do

### Current Features
- Upload one or more PDF files through a Streamlit UI
- Send uploaded files to a FastAPI backend
- Save uploaded PDFs on the backend
- Clean API separation between frontend and backend

### Planned Features
- Extract text from uploaded PDFs
- Extract image or printed text in addition to normal text (using OCR)
- Split text into chunks for semantic search
- Generate embeddings for each chunk
- Store embeddings in a vector database (FAISS / Chroma)
- Perform semantic search over documents
- Use a Large Language Model (LLM) to generate answers
- Display answers with document citations
- Support multiple documents per session
- If files have same name, compare and check bytes, then save

---

## 🏗️ High-Level Architecture

```
User
 │
 ▼
Streamlit Frontend
 │
 │  (HTTP requests)
 ▼
FastAPI Backend
 │
 ├─ PDF ingestion
 ├─ Text extraction & chunking
 ├─ Embedding generation
 ├─ Vector database
 └─ LLM-based question answering
```

- Streamlit handles UI only (uploading files, asking questions)
- FastAPI handles all processing and AI logic

---

## 🛠️ Tech Stack

**Backend**
- Python
- FastAPI
- PyMuPDF / pdfminer (planned)
- Vector DB: FAISS or Chroma (planned)
- LLM: OpenAI / LLaMA (planned)

**Frontend**
- Streamlit

**Infrastructure (planned)**
- Docker
- GitHub Actions
- Cloud deployment (Render / HuggingFace / AWS)

---

## 📁 Project Structure (Current)

```
rag-pdf-chatbot/
├── backend/
│   ├── fastapi.py       # FastAPI application
│   └── data/uploads/    # Uploaded PDF files
├── frontend/
│   └── streamlit_app.py # Streamlit UI
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run the Project Locally

1. **Start the backend**
	```sh
	uvicorn backend.main:app --reload --port 8000
	```

2. **Start the frontend**
	```sh
	streamlit run frontend/streamlit_app.py
	```

3. **Open the app**
	- Streamlit UI: [http://localhost:8501](http://localhost:8501)
	- FastAPI docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📌 Project Status

🚧 Work in Progress

This project is under active development.  
New features will be added incrementally while following best practices for applied AI systems.

---

## 📜 License

MIT License

