from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.services.embedding_service import EmbeddingService


embedding_service = None


@asynccontextmanager
async def lifespan(app: FastAPI):

    global embedding_service

    embedding_service = EmbeddingService()

    yield

    print("🛑 Cerrando aplicación...")


app = FastAPI(
    title="Vector Search API",
    lifespan=lifespan
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Buscador vectorial funcionando"
    }