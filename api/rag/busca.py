import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from rag.mongo import get_colecao_produtos
from rag.embeddings import gerar_embedding

DEFAULT_TOP_K = 3


def buscar_produtos_semantico(pergunta: str, top_k: int = DEFAULT_TOP_K):
    embedding_pergunta = gerar_embedding(pergunta)
    colecao = get_colecao_produtos()

    produtos = list(colecao.find({}, {"nome": 1, "descricao": 1, "embedding": 1}))

    if not produtos:
        return []

    resultados = []
    for p in produtos:
        if "embedding" not in p:
            continue

        similaridade = cosine_similarity(
            [embedding_pergunta],
            [p["embedding"]]
        )[0][0]

        resultados.append({
            "nome": p["nome"],
            "descricao": p["descricao"],
            "score": float(similaridade)
        })

    resultados.sort(key=lambda x: x["score"], reverse=True)
    return resultados[:top_k]
