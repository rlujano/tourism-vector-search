from sentence_transformers import SentenceTransformer

print("Descargando modelo...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

model.save("/app/ai_models/all-MiniLM-L6-v2")

print("Modelo guardado.")