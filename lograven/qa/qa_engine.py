from typing import List
from lograven.embedding.embedding_engine import EmbeddingEngine
from lograven.vector_store.faiss_store import VectorStore
from lograven.inference.inference_engine import InferenceEngine


class QAEngine:
    def __init__(self, embedding_model: str = "all-MiniLM-L6-v2", dim: int = 384, use_inference: bool = True):
        self.embedder = EmbeddingEngine(model_name=embedding_model)
        self.vector_store = VectorStore(dim=dim)
        self.inference_engine = InferenceEngine() if use_inference else None

    def ingest_documents(self, documents: List[str]):
        vectors = self.embedder.embed_chunks(documents)
        self.vector_store.add(vectors, documents)

    def answer(self, query: str, top_k: int = 5) -> List[str]:
        query_vector = self.embedder.embed_query(query)
        results = self.vector_store.query(query_vector, top_k=top_k)
        relevant_docs = [doc for doc, _ in results]

        if self.inference_engine:
            context = "\n".join(relevant_docs)
            inferred = self.inference_engine.generate_answer(context, query)
            return [inferred] + relevant_docs

        return relevant_docs
