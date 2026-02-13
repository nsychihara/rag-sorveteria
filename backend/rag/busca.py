import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from rag.mongo import colecao_produtos
from rag.embeddings import gerar_embedding


def buscar_produtos_semantico(pergunta: str, top_k: int = 10):
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

    if resultados and resultados[0]["score"] < 0.35:
        return [
            {
                "nome": p["nome"],
                "descricao": p["descricao"],
                "score": 1.0
            }
            for p in produtos
        ]

    return resultados[:top_k]


def buscar_produtos(pergunta: str):
    """
    Função principal que decide:
    - Se a pergunta for genérica (listar todos), retorna todos os produtos
    - Caso contrário, usa busca semântica
    """

    pergunta_lower = pergunta.lower()

    palavras_listagem = [
        "todos",
        "todas",
        "listar",
        "quais são",
        "mostre",
        "me diga todos",
        "me liste"
    ]

    if any(p in pergunta_lower for p in palavras_listagem):
        produtos = list(colecao_produtos.find())

        return [
            {
                "nome": p["nome"],
                "descricao": p["descricao"],
                "score": 1.0
            }
            for p in produtos
        ]

    return buscar_produtos_semantico(pergunta)
