import os
from typing import Optional

import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self, model_path: Optional[str] = None):
        self.model_path = model_path or "/app/ai_models/all-MiniLM-L6-v2"
        self._model = None

    def _get_model(self):
        if self._model is None:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(
                    f"El modelo no existe en {self.model_path}. Ejecuta primero download_model.py"
                )

            self._model = SentenceTransformer(self.model_path)

        return self._model

    def encode(self, text: str):
        if not text or not str(text).strip():
            return np.zeros(384, dtype=np.float32)

        model = self._get_model()
        vector = model.encode(text, convert_to_numpy=True, normalize_embeddings=True)
        return np.asarray(vector, dtype=np.float32)