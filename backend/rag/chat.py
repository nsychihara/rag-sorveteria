from rag.busca import buscar_produtos
from rag.llm import gerar_resposta


def responder(pergunta: str):

    resultados = buscar_produtos(pergunta)

    contexto = "\n".join(
        [f"{r['nome']}: {r['descricao']}" for r in resultados]
    )

    resposta = gerar_resposta(pergunta, contexto)

    return resposta
