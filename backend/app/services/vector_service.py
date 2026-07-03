import hnswlib
import numpy as np
import pickle


class VectorService:

    def __init__(self):
        self.index = hnswlib.Index(space="cosine", dim=384)

        self.index.load_index("/app/indexes/hnsw.index")
        self.index.set_ef(50)

        with open("/app/indexes/meta.pkl", "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query_vector, k=5):

        labels, distances = self.index.knn_query(query_vector, k=k)

        results = []

        for i, label in enumerate(labels[0]):
            item = next(x for x in self.metadata if x["id"] == label)

            results.append({
                "id": label,
                "text": item["text"],
                "distance": float(distances[0][i])
            })

        return results