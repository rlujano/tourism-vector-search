from sentence_transformers import SentenceTransformer
import numpy as np
import os


class EmbeddingService:

    def __init__(self):

        model_path = "/app/ai_models/all-MiniLM-L6-v2"

        if not os.path.exists(model_path):
            raise Exception(
                f"El modelo no existe en {model_path}. Ejecuta primero download_model.py"
            )

        print("Cargando modelo local...")

        self.model = SentenceTransformer(model_path)

        print("Modelo cargado.")

    def encode(self, text: str):

        vector = self.model.encode(
            text,
            convert_to_numpy=True
        )

        vector = vector / np.linalg.norm(vector)

        return vector