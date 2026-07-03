from pathlib import Path
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

MODEL_DIR = Path("/app/ai_models/all-MiniLM-L6-v2")


def main():

    if MODEL_DIR.exists():
        print("✅ El modelo ya existe.")
        return

    print("⬇ Descargando modelo...")

    model = SentenceTransformer(MODEL_NAME)

    MODEL_DIR.parent.mkdir(parents=True, exist_ok=True)

    model.save(str(MODEL_DIR))

    print("✅ Modelo guardado correctamente en:")
    print(MODEL_DIR)


if __name__ == "__main__":
    main()