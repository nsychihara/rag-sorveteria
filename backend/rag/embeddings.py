from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def gerar_embedding(texto: str) -> list[float]:
    embedding = modelo.encode(texto)
    return embedding.tolist()
