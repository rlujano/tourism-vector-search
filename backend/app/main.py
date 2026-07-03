from fastapi import FastAPI
from app.api import health, search, index, attractions

app = FastAPI()

app.include_router(health.router)
app.include_router(search.router)
app.include_router(index.router)
app.include_router(attractions.router)


@app.get("/")
def root():
    return {"message": "OK"}