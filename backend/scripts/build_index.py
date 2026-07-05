import os

import hnswlib
import numpy as np

from app.repositories.attraction_repository import AttractionRepository
from app.services.embedding_service import EmbeddingService


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

    m = int(48)
    ef_construction = int(500)
    mmax0 = int(40)

    index = hnswlib.Index(space='cosine', dim=dim)
    init_kwargs = {
        "max_elements": len(attractions),
        "M": m,
        "ef_construction": ef_construction,
    }

    try:
        index.init_index(**init_kwargs, Mmax0=mmax0)
        used_mmax0 = mmax0
    except TypeError:
        index.init_index(**init_kwargs)
        used_mmax0 = "default"

    index.add_items(embeddings, np.arange(len(attractions)))

    index_path = os.getenv("VECTOR_INDEX_PATH", "/app/indexes/destinos.index")
    os.makedirs(os.path.dirname(index_path), exist_ok=True)

    index.save_index(index_path)

    print(f"Índice vectorial construido correctamente con M={m}, ef_construction={ef_construction}, Mmax0={used_mmax0}")


if __name__ == "__main__":
    main()