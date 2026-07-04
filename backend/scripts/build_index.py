from app.repositories.attraction_repository import AttractionRepository
from app.services.embedding_service import EmbeddingService
import hnswlib
import numpy as np
import os


def main():

    repository = AttractionRepository()
    embedding_service = EmbeddingService()

    attractions = repository.find_all()

    print(f"Se encontraron {len(attractions)} atractivos.")

    texts = [
        f"{a.name}. {a.description}. {a.location}. {a.category}"
        for a in attractions
    ]

    embeddings = np.array([
        embedding_service.encode(text)
        for text in texts
    ])

    dim = embeddings.shape[1]

    index = hnswlib.Index(space='cosine', dim=dim)
    index.init_index(max_elements=len(attractions), ef_construction=200, M=16)

    index.add_items(embeddings, np.arange(len(attractions)))

    os.makedirs("/app/indexes", exist_ok=True)

    index.save_index("/app/indexes/destinos.index")

    print("Índice vectorial construido correctamente.")


if __name__ == "__main__":
    main()