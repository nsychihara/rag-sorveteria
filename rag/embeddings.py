from sentence_transformers import SentenceTransformer
import numpy as np
from .models import Produto

model = SentenceTransformer("all-MiniLM-L6-v2")


def gerar_embedding(texto):
    return model.encode(texto)


def buscar_produto_semelhante(pergunta):
    pergunta_embedding = gerar_embedding(pergunta)
 
    produtos = Produto.objects.filter(disponivel=True)

    melhor_score = -1
    melhor_produto = None

    for produto in produtos:
        descricao_embedding = gerar_embedding(produto.descricao)

        score = np.dot(pergunta_embedding, descricao_embedding)

        if score > melhor_score:
            melhor_score = score
            melhor_produto = produto

    return melhor_produto
