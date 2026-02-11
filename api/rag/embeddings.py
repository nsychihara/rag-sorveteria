from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
_modelo = None


def get_modelo():
    global _modelo
    if _modelo is None:
        _modelo = SentenceTransformer(MODEL_NAME)
    return _modelo


def gerar_embedding(texto: str) -> list[float]:
    modelo = get_modelo()
    embedding = modelo.encode(texto)
    return embedding.tolist()
