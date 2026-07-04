from fastapi import APIRouter, Query

from app.core.services import embedding_service, vector_service
from app.repositories.attraction_repository import AttractionRepository
from app.services.search_ranking import rank_attractions

router = APIRouter()
repository = AttractionRepository()


@router.get("/search")
def search(q: str = Query(..., min_length=1)):
    query_text = q.strip()
    results = repository.find_all()

    try:
        query_vector = embedding_service.encode(query_text)
        labels, distances = vector_service.search(query_vector, k=5)
    except Exception:
        labels, distances = [], []

    semantic_candidates = []
    for idx, distance in zip(labels, distances):
        if 0 <= idx < len(results):
            semantic_candidates.append((idx, float(distance)))

    ranked = rank_attractions(query_text, results, semantic_candidates)
    mapped = []
    for score, attraction in ranked[:5]:
        mapped.append({
            "id": attraction.id,
            "name": attraction.name,
            "description": attraction.description,
            "location": attraction.location,
            "category": attraction.category,
            "image_url": attraction.image_url,
            "score": round(float(score), 4),
        })

    if not mapped:
        mapped = [
            {
                "id": attraction.id,
                "name": attraction.name,
                "description": attraction.description,
                "location": attraction.location,
                "category": attraction.category,
                "image_url": attraction.image_url,
                "score": 0.0,
            }
            for attraction in results[:5]
        ]

    return {
        "query": query_text,
        "results": mapped,
    }