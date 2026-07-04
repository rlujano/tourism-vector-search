from dataclasses import dataclass


@dataclass
class Attraction:
    id: int
    name: str
    description: str
    location: str
    latitude: float
    longitude: float
    category: str
    image_url: str