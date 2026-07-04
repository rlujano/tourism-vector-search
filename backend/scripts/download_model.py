from pathlib import Path
from sentence_transformers import SentenceTransformer

# CAMBIO: Usamos el modelo optimizado para más de 50 idiomas (incluido el español)
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# CAMBIO: Actualizamos la ruta de la carpeta para el nuevo modelo
MODEL_DIR = Path("/app/ai_models/paraphrase-multilingual-MiniLM-L12-v2")


def main():

    if MODEL_DIR.exists():
        print("✅ El modelo multilingüe ya existe.")
        return

    print("⬇ Descargando modelo multilingüe (esto puede tardar un poco más)...")

    model = SentenceTransformer(MODEL_NAME)

    MODEL_DIR.parent.mkdir(parents=True, exist_ok=True)

    model.save(str(MODEL_DIR))

    print("✅ Modelo multilingüe guardado correctamente en:")
    print(MODEL_DIR)


if __name__ == "__main__":
    main()