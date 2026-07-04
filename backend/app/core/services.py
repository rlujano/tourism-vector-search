import os

from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

embedding_service = EmbeddingService()
vector_service = VectorService(os.getenv("VECTOR_INDEX_PATH", "/app/indexes/destinos.index"))