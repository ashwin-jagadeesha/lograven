# Lograven

[![Build](https://img.shields.io/github/actions/workflow/status/your-username/lograven/python-app.yml?label=Build&logo=github)](https://github.com/your-username/lograven/actions)
[![License](https://img.shields.io/github/license/your-username/lograven?color=blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Issues](https://img.shields.io/github/issues/your-username/lograven)](https://github.com/your-username/lograven/issues)
[![Stars](https://img.shields.io/github/stars/your-username/lograven?style=social)](https://github.com/your-username/lograven)


> **Modular, local-first log Q&A engine for large-scale logs (100k–500k tokens), featuring token-aware chunking, FAISS-powered retrieval, and optional local LLM inference.**

---

## 🔍 Overview

**Lograven** is a developer-focused library for **efficient log question answering (QA)** over large, unstructured logs. Designed to be modular and offline-first, it can ingest, chunk, embed, and retrieve context-rich log segments — then optionally invoke a local language model (like TinyLlama) for answer generation.

---

## ✨ Key Features

- 🧱 **Token-aware chunking** to preserve semantic boundaries
- 📚 **FAISS vector store** for fast similarity-based retrieval
- 🧠 **LLM-optional inference** using local models like `TinyLlama`
- ⚙️ **Pluggable architecture** for chunkers, heuristics, and models
- 💻 **Offline and private by default** (no OpenAI required)
- 🔁 **Interactive Q&A loop** to test log analysis performance

---

## 🧠 How It Works

1. **Ingest Logs**  
   Break large logs (e.g., 200k+ tokens) into intelligently sized chunks.

2. **Embed Chunks**  
   Use sentence-transformers to vectorize each chunk into FAISS.

3. **Ask a Question**  
   Your query is embedded and matched against stored vectors.

4. **Retrieve + Infer**  
   Top matching chunks are passed into a local LLM for final answer generation.

---

## 💡 Use Cases

- Debugging production or infra logs
- RCA (Root Cause Analysis) workflows
- AI-assisted SRE & DevOps
- Private incident postmortems with no API calls

---

## 📁 Directory Structure

```
lograven/
│
├── lograven/
│   ├── __init__.py
│   ├── chunking/
│   │   └── token_chunker.py
│   ├── embedding/
│   │   └── embedding_engine.py
│   ├── vector_store/
│   │   └── faiss_store.py
│   ├── inference/
│   │   └── inference_engine.py
│   └── qa/
│       └── qa_engine.py
│
├── examples/
│   └── qa_example.py
│
├── requirements.txt
├── setup.py
└── README.md

```

## 🚀 Quickstart

### 1. Clone & Setup

```bash
git clone https://github.com/your-username/lograven.git
cd lograven
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Run the example
```
python examples/qa_example.py
```


### 3. Q & A

```
Ask a question about the logs:
> any exections in this log

Inference Answer:
Yes, there are several exceptions in this log that indicate issues with connecting to the database. Here are the relevant excerpts:

- Exception: ConnectionTimeout
This exception indicates that the database server timed out while trying to connect to your application. This can be caused by a variety of issues, such as a misconfigured network connection, a firewall blocking your application, or an issue with the database server itself. It's essential to check your network configuration and database server settings to ensure that they are properly configured and running correctly. If you're still experiencing issues with connecting to the database, it's worth considering upgrading to a newer version of your database server or configuring your application to use a different database provider.

Top Relevant Logs:
1. 2025-07-27 12:00:06 WARNING Disk space low
2. 2025-07-27 12:00:04 INFO Connection established
3. 2025-07-27 12:00:02 INFO Retrying connection
4. 2025-07-27 12:00:01 ERROR Failed to connect to database
5. 2025-07-27 12:00:03 Exception: ConnectionTimeout

========================================

Ask a question about the logs:
>
```

## Dependencies

```
transformers==4.54.0
accelerate==0.28.0
torch>=2.1.0
sentence-transformers==2.6.1
tiktoken==0.9.0
faiss-cpu==1.8.0
numpy==1.26.4
scikit-learn==1.3.2
regex==2024.5.15
rich==14.1.0
```

## Local inference

Local Inference with TinyLlama
By default, the system uses TinyLlama-1.1B-Chat as the inference engine:

Loads onto GPU automatically (if available)

No Hugging Face login required

Generates contextual, natural language answers

You can change the model by editing inference_engine.py.

## Example Logs Used

```
log_data = [
    "2025-07-27 12:00:01 ERROR Failed to connect to database",
    "2025-07-27 12:00:02 INFO Retrying connection",
    "2025-07-27 12:00:03 Exception: ConnectionTimeout",
    "2025-07-27 12:00:04 INFO Connection established",
    "2025-07-27 12:00:05 CRITICAL System failure imminent",
    "2025-07-27 12:00:06 WARNING Disk space low"
]
``` 

## Extending Lograven

### You can extend the system via:

```
1. Custom chunking heuristics (chunking/)

2. Different vector stores (vector_store/)

3. Custom inference models (inference/)

4. UI or API interface (Flask, FastAPI, etc.)
```

🔐 License
MIT License © 2025



