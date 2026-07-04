from fastapi import APIRouter

from app.services.attraction_service import AttractionService

router = APIRouter()
service = AttractionService()


@router.get("/attractions")
def attractions():
    return service.list_attractions()