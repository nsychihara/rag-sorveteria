from rag.busca import buscar_produtos_semantico
from rag.llm import gerar_resposta

def responder(pergunta: str):

    resultados = buscar_produtos_semantico(pergunta, top_k=3)

    contexto = "\n".join(
        [f"{r['nome']}: {r['descricao']}" for r in resultados]
    )

    resposta = gerar_resposta(pergunta, contexto)

    return resposta
