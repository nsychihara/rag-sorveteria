import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rag_sorveteria.settings")
django.setup()

from rag.mongo import colecao_produtos
from rag.embeddings import gerar_embedding

produtos = colecao_produtos.find()

for produto in produtos:
    descricao = produto["descricao"]
    embedding = gerar_embedding(descricao)

    colecao_produtos.update_one(
        {"_id": produto["_id"]},
        {"$set": {"embedding": embedding}}
    )

    print(f"Embedding gerado: {produto['nome']}")

print("Todos os embeddings foram gerados!")
