# Lograven Codebase Overview

Lograven is a modular toolkit for question answering over large log files. The package is structured as a set of cooperating submodules that mirror the main stages of a retrieval-augmented generation (RAG) workflow: chunking, embedding, vector storage, optional inference, and orchestration.

## Repository Layout

```
lograven/
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
├── examples/
│   └── qa_example.py
├── docs/
│   └── architecture_overview.md (this file)
├── requirements.txt
├── setup.py
└── README.md
```

The `lograven` package contains the core building blocks. The `examples` directory illustrates how the components are meant to be combined in practice.

## Core Modules

### Chunking (`lograven/chunking/token_chunker.py`)
The `TokenChunker` class tokenizes incoming log text using `tiktoken`'s `cl100k_base` encoding and slices the tokens into fixed-size windows. This ensures that downstream embedding and retrieval stay within model token limits while keeping log messages intact.【F:lograven/chunking/token_chunker.py†L1-L17】

### Embedding (`lograven/embedding/embedding_engine.py`)
`EmbeddingEngine` wraps a Sentence Transformers model (default `all-MiniLM-L6-v2`) to produce vector representations for log chunks, queries, or arbitrary documents. It exposes convenience methods for chunk and query embedding, all returning NumPy arrays.【F:lograven/embedding/embedding_engine.py†L1-L15】

### Vector Store (`lograven/vector_store/faiss_store.py`)
`VectorStore` is a light wrapper around FAISS's `IndexFlatL2`. It keeps parallel lists of document text and their vectors, supports batch insertion with shape validation, and performs nearest-neighbor search to surface the most relevant log snippets for a query.【F:lograven/vector_store/faiss_store.py†L1-L22】

### Inference (`lograven/inference/inference_engine.py`)
`InferenceEngine` optionally loads a local causal language model (default `TinyLlama/TinyLlama-1.1B-Chat-v1.0`). It selects GPU or CPU automatically, constructs a prompt that bundles retrieved log context with the user question, and generates an answer while staying in evaluation mode. The helper trims the generated text back to the assistant response only.【F:lograven/inference/inference_engine.py†L1-L45】

### QA Orchestrator (`lograven/qa/qa_engine.py`)
`QAEngine` ties together chunk embedding, FAISS retrieval, and optional inference. After ingesting documents, it stores their embeddings in the vector store. Queries are embedded and matched to retrieve top-k logs; if inference is enabled the engine concatenates the retrieved snippets into a context and asks the language model to draft an answer before returning both the answer and supporting logs.【F:lograven/qa/qa_engine.py†L1-L25】

## Example Workflow

`examples/qa_example.py` demonstrates an interactive command-line loop. It seeds the engine with sample log entries, then repeatedly prompts the user for questions, retrieving relevant logs and (if configured) generating an explanatory answer.【F:examples/qa_example.py†L1-L35】

## Getting Started Tips

1. **Run the example**: `python examples/qa_example.py` loads the default pipeline and lets you experiment with ad-hoc questions.
2. **Swap components**: Because each stage is encapsulated, you can replace the chunker, embedder, or inference engine with alternatives that fit your environment.
3. **Scale to real logs**: Extend `TokenChunker` to apply heuristic chunk boundaries (e.g., by timestamp) or to stream from files. You might also persist FAISS indexes for reuse.

## Next Steps for New Contributors

- Review `requirements.txt` and ensure your environment can satisfy GPU or CPU inference needs depending on target hardware.【F:requirements.txt†L1-L11】
- Explore adding new chunkers or embeddings in dedicated modules to support domain-specific log formats.
- Implement evaluation utilities (e.g., precision/recall metrics) to measure retrieval quality on curated datasets.
- Consider contributing documentation for deploying Lograven in production pipelines or integrating with observability stacks.

By understanding how each component interacts, newcomers can confidently iterate on individual stages without breaking the overall QA flow.
