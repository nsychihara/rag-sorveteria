import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from rag.mongo import get_colecao_produtos
from rag.embeddings import gerar_embedding

def atualizar_embeddings():
    colecao = get_colecao_produtos()
    produtos = colecao.find()

    count = 0
    for produto in produtos:
        descricao = produto["descricao"]
        embedding = gerar_embedding(descricao)

        colecao.update_one(
            {"_id": produto["_id"]},
            {"$set": {"embedding": embedding}}
        )

        print(f"✓ Embedding gerado: {produto['nome']}")
        count += 1

    print(f"✓ {count} embeddings atualizados")

if __name__ == "__main__":
    atualizar_embeddings()
