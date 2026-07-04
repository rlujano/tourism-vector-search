from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import attractions, health, index, search

app = FastAPI(title="Tourism Vector Search")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(search.router)
app.include_router(index.router)
app.include_router(attractions.router)


@app.get("/")
def root():
    return {"message": "OK"}