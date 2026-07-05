import time
from typing import List, Tuple

import requests


QUERIES: List[Tuple[str, List[str]]] = [
    (
        "hombres tejedores",
        ["Isla de Taquile", "Barrio de Santa Ana en Ayacucho", "Pueblo Tradicional de Catacaos"],
    ),
    (
        "textiles",
        ["Isla de Taquile", "Barrio de Santa Ana en Ayacucho", "Pueblo Tradicional de Catacaos"],
    ),
    (
        "ciudadela incaica",
        ["Machu Picchu", "Sacsayhuamán", "Choquequirao"],
    ),
    (
        "baños termales",
        ["Baños del Inca", "Moyobamba (Ciudad de las Orquídeas)"],
    ),
    (
        "lago andino",
        ["Lago Titicaca", "Laguna de Paca", "Laguna Azul (El Sauce)"],
    ),
]


def run_evaluation(base_url: str = "http://localhost:8000"):
    print(f"Evaluando búsqueda contra {base_url}/search\n")
    total_recall = 0.0
    times: List[float] = []

    for query, expected in QUERIES:
        start = time.time()
        resp = requests.get(f"{base_url}/search", params={"q": query})
        elapsed = time.time() - start
        times.append(elapsed)

        resp.raise_for_status()
        data = resp.json()
        results = [item["name"] for item in data.get("results", [])]

        expected_set = set(expected)
        hit_set = expected_set & set(results[:5])
        recall_at_5 = len(hit_set) / max(1, len(expected_set))
        total_recall += recall_at_5

        print(f"Query: {query} ({elapsed:.3f}s)")
        print("  Esperados :", list(expected_set))
        print("  Resultados:", results)
        print(f"  Recall@5 : {recall_at_5:.2f}\n")

    avg_recall = total_recall / len(QUERIES)
    avg_time = sum(times) / len(times) if times else 0.0
    print("=== Resumen ===")
    print(f"Recall@5 promedio: {avg_recall:.2f}")
    print(f"Tiempo medio por query: {avg_time:.3f}s")


if __name__ == "__main__":
    run_evaluation()
