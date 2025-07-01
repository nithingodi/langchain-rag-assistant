# langchain-rag-assistant
# 🤖 LangChain RAG Assistant

This project builds a fully open-source Retrieval-Augmented Generation (RAG) assistant using LangChain, HuggingFace Transformers, FAISS, and Streamlit.

It allows users to ask natural-language questions about markdown-based documentation, mimicking an internal product or support chatbot — entirely without OpenAI APIs.

---

## 🔍 Business Use Case

Companies often have extensive internal documentation, but no easy way to query it. This project solves that by enabling:

- Self-serve document Q&A for analysts, product teams, or devs  
- Streamlined access to internal markdown-based guides  
- Vendor-free GenAI experience using only open-source components

---

## 🧱 Architecture Overview

User Question  
↓  
Retrieval from Markdown Chunks (via FAISS)  
↓  
Answer Generated with LLM (FLAN-T5)

---

## 🛠️ Tech Stack

| Component          | Tool                                      |
|-------------------|-------------------------------------------|
| Loader            | DirectoryLoader / TextLoader              |
| Chunking          | RecursiveCharacterTextSplitter            |
| Embedding Model   | sentence-transformers/all-MiniLM-L6-v2    |
| Vector Store      | FAISS                                      |
| Language Model    | google/flan-t5-base via HuggingFace       |
| UI                | Streamlit                                  |

---

## 🗂️ Project Files

- `app.py`: Streamlit frontend for QA interface  
- `.md` files: Sample documentation  
- `LangChain_RAG_Assistant.ipynb`: Full notebook version  
- `requirements.txt`: Install dependencies  
- `README.md`: You’re reading it ✅

---

## 🚀 Run It Yourself

### Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/langchain-rag-assistant.git
cd langchain-rag-assistant

install dependencies

pip install -r requirements.txt

launch steamlit app

streamlit run app.py


Try the live demo here

https://langchain-rag-assistant-zqhmhpy8s5hwnuvc4igtsc.streamlit.app/
