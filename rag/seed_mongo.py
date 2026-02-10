from rag.mongo import colecao_produtos
from rag.embeddings import gerar_embedding

produtos = [
    {
        "nome": "Sorvete de Chocolate",
        "descricao": "Sorvete cremoso de chocolate belga com pedaços de brownie"
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
