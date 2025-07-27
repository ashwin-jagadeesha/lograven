from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List

class EmbeddingEngine:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents: List[str]) -> np.ndarray:
        return self.model.encode(documents, convert_to_numpy=True)

    def embed_query(self, query: str) -> np.ndarray:
        return self.model.encode([query], convert_to_numpy=True)[0]

    def embed_chunks(self, chunks: List[str]) -> np.ndarray:
        return self.embed_documents(chunks)
