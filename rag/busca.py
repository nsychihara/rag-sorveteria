import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from rag.mongo import colecao_produtos
from rag.embeddings import gerar_embedding


def buscar_produtos_semantico(pergunta: str, top_k: int = 3):
    embedding_pergunta = gerar_embedding(pergunta)

    produtos = list(colecao_produtos.find())

    resultados = []

    for p in produtos:
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
