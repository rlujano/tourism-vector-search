import sys
import types
import unittest


fastapi_module = types.ModuleType("fastapi")


class Query:
    def __init__(self, default=None, min_length=None):
        self.default = default
        self.min_length = min_length


class APIRouter:
    def __init__(self):
        self.routes = []

    def get(self, path):
        def decorator(func):
            self.routes.append((path, func))
            return func

        return decorator


fastapi_module.APIRouter = APIRouter
fastapi_module.Query = Query
sys.modules.setdefault("fastapi", fastapi_module)

from app.api import search as search_module
from app.models.attraction import Attraction


class SearchScoreTests(unittest.TestCase):
    def test_search_returns_non_zero_score(self):
        attraction = Attraction(
            id=1,
            name="Huaca Pucllana",
            description="Gran centro ceremonial arqueológico",
            location="Lima",
            latitude=0.0,
            longitude=0.0,
            category="Arqueológico",
            image_url="https://example.com/huaca.jpg",
        )

        search_module.repository.find_all = lambda: [attraction]
        search_module.embedding_service.encode = lambda text: [0.1] * 384
        search_module.vector_service.search = lambda vector, k=5: ([0], [0.2])

        response = search_module.search("lugares arqueologicos en peru")

        self.assertEqual(response["query"], "lugares arqueologicos en peru")
        self.assertGreater(response["results"][0]["score"], 0.0)


if __name__ == "__main__":
    unittest.main()
