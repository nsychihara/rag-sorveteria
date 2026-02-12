from mongo import colecao_produtos
from embeddings import gerar_embedding

colecao_produtos.delete_many({})

produtos = [
    {
        "nome": "Sorvete de Chocolate",
        "descricao": "Sorvete cremoso de chocolate belga com pedaços de brownie"
    },
    {
        "nome": "Sorvete de Pistache",
        "descricao": "Sorvete com massa a base de pistache bem cremoso e refrescante, uma ótimo opção para dias mais quentes. E num preço bem acessível"
    },
    {
        "nome": "Sorvete de Morango",
        "descricao": "Sorvete artesanal feito com morangos frescos"
    },
    {
        "nome": "Milkshake de Baunilha",
        "descricao": "Milkshake gelado de baunilha com calda de caramelo"
    },
    {
        "nome": "Milkshake de Nuttela",
        "descricao": "Milkshake gelado de Nuttela, super cremoso com o poderoso sabor de avelãs frescas"
    },
    {
        "nome": "Danoninho Sorvetinho",
        "descricao": "O clássico danoninho sorvetinho, agora com sua versão melhorada, com sabor de infância"
    },
    {
        "nome": "Sorvete de Flocos",
        "descricao": "Um dos sabores mais clássicos de sorvete, com pedaços de chocolate meio amargo"
    }
]

docs = []

for p in produtos:
    embedding = gerar_embedding(p["descricao"])
    docs.append({
        "nome": p["nome"],
        "descricao": p["descricao"],
        "embedding": embedding
    })

colecao_produtos.insert_many(docs)

print("Produtos salvos no Mongo com embeddings")
