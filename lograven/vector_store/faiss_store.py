import faiss
import numpy as np
from typing import List, Tuple

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add(self, vectors: List[np.ndarray], docs: List[str]):
        if len(vectors) != len(docs):
            raise ValueError("Vectors and documents must be same length")
        np_vectors = np.vstack(vectors).astype('float32')
        self.index.add(np_vectors)
        self.documents.extend(docs)

    def query(self, query_vector: np.ndarray, top_k: int = 5) -> List[Tuple[str, float]]:
        D, I = self.index.search(np.array([query_vector]).astype('float32'), top_k)
        results = []
        for idx, score in zip(I[0], D[0]):
            if idx < len(self.documents):
                results.append((self.documents[idx], float(score)))
        return results
