import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from rag.mongo import get_colecao_produtos
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

def seed_produtos():
    colecao = get_colecao_produtos()
    docs = []

    for p in produtos:
        embedding = gerar_embedding(p["descricao"])
        docs.append({
            "nome": p["nome"],
            "descricao": p["descricao"],
            "embedding": embedding
        })

    colecao.delete_many({})
    colecao.insert_many(docs)
    print(f"✓ {len(docs)} produtos inseridos com embeddings")

if __name__ == "__main__":
    seed_produtos()
