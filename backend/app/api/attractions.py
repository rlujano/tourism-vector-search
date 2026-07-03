from fastapi import APIRouter

router = APIRouter()

@router.get("/attractions")
def attractions():
    return []