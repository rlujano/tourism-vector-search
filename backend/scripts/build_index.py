import hnswlib
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
import os


# 🔹 dataset demo (luego lo sacamos de DB)
ATTRACTIONS = [
    {"id": 1, "text": "Machu Picchu ancient Inca citadel in Peru"},
    {"id": 2, "text": "Lake Titicaca highest navigable lake in the world"},
    {"id": 3, "text": "Cusco historic capital of Inca Empire"},
    {"id": 4, "text": "Rainbow Mountain Vinicunca colorful mountain in Andes"},
]


MODEL_PATH = "/app/ai_models/all-MiniLM-L6-v2"
INDEX_PATH = "/app/indexes/hnsw.index"
META_PATH = "/app/indexes/meta.pkl"


def main():
    print("🔄 Loading embedding model...")
    model = SentenceTransformer(MODEL_PATH)

    texts = [a["text"] for a in ATTRACTIONS]
    ids = np.array([a["id"] for a in ATTRACTIONS])

    print("🔄 Generating embeddings...")
    embeddings = model.encode(texts, convert_to_numpy=True)

    dim = embeddings.shape[1]

    print("🔄 Building HNSW index...")
    index = hnswlib.Index(space="cosine", dim=dim)

    index.init_index(max_elements=len(embeddings), ef_construction=200, M=16)
    index.add_items(embeddings, ids)

    index.set_ef(50)

    print("💾 Saving index...")
    index.save_index(INDEX_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(ATTRACTIONS, f)

    print("✅ Index built successfully!")


if __name__ == "__main__":
    main()