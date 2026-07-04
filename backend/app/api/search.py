from fastapi import APIRouter, Query
import re

from app.core.services import embedding_service, vector_service
from app.repositories.attraction_repository import AttractionRepository
from app.services.search_ranking import rank_attractions

router = APIRouter()
repository = AttractionRepository()

# Lista de regiones o palabras geográficas comunes en tu dataset para el extractor
REGIONES_PERU = ["puno", "cusco", "ica", "ancash", "ayacucho", "junin", "tacna", "tumbes", "lima", "huancavelica"]

@router.get("/search")
def search(q: str = Query(..., min_length=1)):
    query_text = q.strip()
    results = repository.find_all()

    # 1. DETECTAR INTENCIÓN GEOGRÁFICA
    # Buscamos si el usuario mencionó alguna de nuestras regiones en la consulta
    region_detectada = None
    query_minuscula = query_text.lower()
    for region in REGIONES_PERU:
        if re.search(r'\b' + region + r'\b', query_minuscula):
            region_detectada = region
            break

    try:
        query_vector = embedding_service.encode(query_text)
        # 2. CAMBIO CRÍTICO: Pedimos k=25 vecinos a HNSW en lugar de 5 (Over-sampling).
        # Esto asegura que los destinos de Puno entren en la lista de candidatos semánticos.
        labels, distances = vector_service.search(query_vector, k=min(25, len(results)))
    except Exception:
        labels, distances = [], []

    semantic_candidates = []
    for idx, distance in zip(labels, distances):
        if 0 <= idx < len(results):
            similarity = max(0.0, min(1.0, 1.0 - float(distance)))
            
            # 3. FILTRADO / BOOSTING SEMÁNTICO
            # Si se detectó una región y el atractivo NO pertenece a esa región,
            # penalizamos fuertemente su score o lo descartamos para que no opaque a los correctos.
            if region_detectada:
                atractivo_loc = results[idx].location.lower()
                # Si coincide la región, le damos un boost o mantenemos la similitud alta.
                # Si no coincide, reducimos drásticamente su relevancia semántica para esta consulta.
                if region_detectada not in atractivo_loc:
                    similarity *= 0.1  # Penalización del 90% por no cumplir el criterio geográfico
            
            semantic_candidates.append((idx, similarity))

    # 4. RE-RANKING: Le pasamos la lista extendida y filtrada a tu algoritmo de ordenamiento
    ranked = rank_attractions(query_text, results, semantic_candidates)
    
    # 5. RETORNAR EL TOP 5 FINAL
    mapped = []
    for score, attraction in ranked[:5]:
        # Si aplicamos penalización estricta, podrías omitir scores extremadamente bajos si deseas:
        # if region_detectada and score < 0.1: continue
        
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