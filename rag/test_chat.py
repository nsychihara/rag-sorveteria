from rag.chat import responder

pergunta = input("Pergunta: ")

resposta = responder(pergunta)

print("\nResposta:\n")
print(resposta)
