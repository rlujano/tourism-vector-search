from fastapi import APIRouter

router = APIRouter()

@router.get("/index")
def index_status():
    return {"status": "index ok"}