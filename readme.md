# 🧠 JobSurf – RAG Powered Job Assistant

> Ask in plain English → Get relevant job suggestions
> A lightweight **Retrieval Augmented Generation (RAG)** chatbot that understands skills instead of keywords.

---

## 🚀 What is this?

**JobSurf** is an intelligent job search assistant that recommends jobs based on meaning — not exact matching.

Instead of searching:

> *“Go developer Chennai MongoDB REST API backend”*

You can simply ask:

> *“I know Go and APIs, what jobs fit me?”*

The bot reads job descriptions, retrieves relevant ones using embeddings, and explains why they match.

---

## 🧩 How it works (Simple Architecture)

```
User Question
     ↓
Embedding (semantic meaning)
     ↓
Vector Search (FAISS)
     ↓
Top Matching Jobs Retrieved
     ↓
LLM explains recommendation
```

**RAG = Search Engine + LLM Reasoning**

---

## 🛠 Tech Stack

* Python
* FAISS (Vector Database)
* Sentence Transformers (Embeddings)
* Ollama + Llama3 (Local LLM)
* Simple text dataset (jobs.txt)

> No cloud API keys required 🔐
> Fully offline AI system

---

## 📦 Installation

### 1. Clone

```bash
git clone https://github.com/yourusername/jobsurf
cd jobsurf
```

### 2. Install dependencies

```bash
pip install sentence-transformers faiss-cpu ollama
```

### 3. Install LLM

```bash
ollama pull llama3
```

---

## 📄 Dataset

Create a `jobs.txt`

Example:

```
Backend Developer - Go, MongoDB, REST APIs - Chennai
Frontend Developer - React, Tailwind - Bangalore
Data Scientist - Python, ML, Pandas - Remote
DevOps Engineer - Docker, Kubernetes, AWS - Hyderabad
AI Engineer - NLP, Transformers, Python - Remote
```

---

## 🧠 Index Jobs

```bash
python index.py
```

This converts jobs → embeddings → FAISS vector database.

---

## 💬 Run the Bot

```bash
python job_bot.py
```

---

## 🧪 Example Queries

```
I know Go and backend development
Suggest remote AI jobs
Jobs for Python ML beginner
DevOps roles in cloud
```

---

## 🎯 Why this project?

Traditional job portals rely on keyword matching.
This project demonstrates how semantic retrieval + LLM reasoning creates a smarter job assistant.

The bot understands:

* skills
* intent
* similarity
* career alignment

Not just text matching.

---

## 🧠 Future Improvements

* Resume upload → auto skill extraction
* Match score (ATS style)
* LinkedIn scraping
* Auto job alert system
* Recruiter mode
* Multi-user backend API (FastAPI / Go)

---

## 📚 Learning Goals

This project teaches:

* RAG architecture fundamentals
* Embeddings vs keyword search
* Vector databases
* Local LLM usage
* Building domain-specific AI assistants

---

## 🪪 License

MIT

---

## ✨ Author

Built for learning applied AI systems and practical semantic search.
