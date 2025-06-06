# devtoolbox/vector_db_connector.py

import os
import faiss
import numpy as np
import pickle

class VectorDBConnector:
    def __init__(self, dim=128, db_path="vector_db.index", metadata_path="vector_meta.pkl"):
        self.dim = dim
        self.db_path = db_path
        self.metadata_path = metadata_path
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

        if os.path.exists(db_path) and os.path.exists(metadata_path):
            self.load()

    def add_vectors(self, vectors: np.ndarray, meta: list):
        if vectors.shape[1] != self.dim:
            raise ValueError("Vector dimension mismatch.")
        self.index.add(vectors)
        self.metadata.extend(meta)
        self.save()

    def search(self, query_vector: np.ndarray, top_k=5):
        if query_vector.shape[0] != self.dim:
            raise ValueError("Query vector dimension mismatch.")
        D, I = self.index.search(np.array([query_vector]), top_k)
        results = [{"score": float(D[0][i]), "meta": self.metadata[I[0][i]]}
                   for i in range(len(I[0])) if I[0][i] < len(self.metadata)]
        return results

    def save(self):
        faiss.write_index(self.index, self.db_path)
        with open(self.metadata_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self):
        self.index = faiss.read_index(self.db_path)
        with open(self.metadata_path, "rb") as f:
            self.metadata = pickle.load(f)
