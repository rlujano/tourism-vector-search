from app.repositories.attraction_repository import AttractionRepository


class AttractionService:
    def __init__(self):
        self.repository = AttractionRepository()

    def list_attractions(self):
        attractions = self.repository.find_all()
        return [
            {
                "id": attraction.id,
                "name": attraction.name,
                "description": attraction.description,
                "location": attraction.location,
                "latitude": attraction.latitude,
                "longitude": attraction.longitude,
                "category": attraction.category,
                "image_url": attraction.image_url,
            }
            for attraction in attractions
        ]