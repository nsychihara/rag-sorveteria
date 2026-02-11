from rag.busca import buscar_produtos_semantico

resultado = buscar_produtos_semantico(
    "Quero um sorvete bem cremoso de chocolate",
    top_k=2
)

for r in resultado:
    print(r)
