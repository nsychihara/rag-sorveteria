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
