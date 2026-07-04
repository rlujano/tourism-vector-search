import sys
import types
import unittest


fastapi_module = types.ModuleType("fastapi")

numpy_module = types.ModuleType("numpy")
numpy_module.asarray = lambda value, dtype=None: value
numpy_module.zeros = lambda *shape, **kwargs: [0.0] * (shape[0] if shape else 384)
sys.modules.setdefault("numpy", numpy_module)

sentence_transformers_module = types.ModuleType("sentence_transformers")


class DummySentenceTransformer:
    def __init__(self, *args, **kwargs):
        pass

    def encode(self, texts, convert_to_numpy=True, normalize_embeddings=True):
        if isinstance(texts, str):
            return [0.0] * 384
        return [[0.0] * 384 for _ in texts]


sentence_transformers_module.SentenceTransformer = DummySentenceTransformer
sys.modules.setdefault("sentence_transformers", sentence_transformers_module)


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

    def test_food_query_prioritizes_food_related_results(self):
        attractions = [
            Attraction(
                id=1,
                name="Lago Titicaca",
                description="Gran lago andino con paisajes impresionantes",
                location="Puno",
                latitude=0.0,
                longitude=0.0,
                category="Naturaleza",
                image_url="https://example.com/titicaca.jpg",
            ),
            Attraction(
                id=2,
                name="Valle del Mantaro",
                description="Región andina reconocida por su gastronomía típica basada en la papa",
                location="Junín",
                latitude=0.0,
                longitude=0.0,
                category="Cultural",
                image_url="https://example.com/mantaro.jpg",
            ),
            Attraction(
                id=3,
                name="Restaurante El Sol",
                description="Restaurante tradicional con comida andina y platos típicos",
                location="Cusco",
                latitude=0.0,
                longitude=0.0,
                category="Restaurante",
                image_url="https://example.com/restaurante.jpg",
            ),
        ]

        search_module.repository.find_all = lambda: attractions
        search_module.embedding_service.encode = lambda text: [0.1] * 384
        search_module.vector_service.search = lambda vector, k=5: ([0, 1, 2], [0.2, 0.2, 0.2])

        response = search_module.search("comida andina")
        top_names = [result["name"] for result in response["results"]]

        self.assertIn("Restaurante El Sol", top_names)
        self.assertLess(top_names.index("Restaurante El Sol"), top_names.index("Lago Titicaca"))


if __name__ == "__main__":
    unittest.main()
