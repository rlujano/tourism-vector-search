import os
from typing import Optional

import hnswlib
import numpy as np


class VectorService:
    def __init__(self, index_path: Optional[str] = None):
        self.index_path = index_path or os.getenv("VECTOR_INDEX_PATH", "/app/indexes/destinos.index")
        self.index = None
        self._ef = 50

    def _ensure_index(self):
        if self.index is None:
            if not os.path.exists(self.index_path):
                raise FileNotFoundError(f"No existe el índice vectorial en {self.index_path}")

            self.index = hnswlib.Index(space="cosine", dim=384)
            self.index.load_index(self.index_path)
            self.index.set_ef(self._ef)

        return self.index

    def search(self, vector, k=5):
        index = self._ensure_index()
        query_vector = np.asarray(vector, dtype=np.float32).reshape(1, -1)
        labels, distances = index.knn_query(query_vector, k=min(k, index.get_max_elements()))
        return labels[0].tolist(), distances[0].tolist()