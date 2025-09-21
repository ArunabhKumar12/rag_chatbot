# Simple RAG Chatbot

## Overview:
Lightweight chatbot where users upload documents (PDF, Word).
Chatbot answers questions directly from document content.

## Tech stacks:
- Python — core language
- Streamlit — frontend UI
- LangChain — RAG pipeline
- VectorDB (Chroma/Pinecone) — store embeddings

## Setup
```bash
git clone <repo-url>
cd rag_chatbot
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run Instructions
```bash
streamlit run app/main.py
```

## Folder Structure
E:.
│   README.md
│
├───app
├───configs
│       .env.example
│
├───docs
│       DESIGN.md
│
├───notebooks
├───src
│       __init__.py
│
├───tests
│       test_placeholder.py
│
└───utils

## Future Enhancements
- Multi-document support
- Web search integration
- Better evaluation metrics (precision/recall, citation quality)

## Added document ingestion skeleton
