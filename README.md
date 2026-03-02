# rag-sorveteria

Projeto de estudo/demo de **RAG (Retrieval-Augmented Generation)** aplicado a uma “sorveteria”: um backend em **Python/Django** e um frontend com **React TSX**.

> Estrutura principal do repositório: `frontend/`, `rag/`, `rag_sorveteria/`, `manage.py`, `requirements.txt` e `package-lock.json`.
---

## Visão geral

Este projeto reúne:

- **Backend (Django)**: API/serviço responsável por receber perguntas e gerar respostas usando RAG.
- **Camada RAG**: módulo/pasta `rag/` com a lógica de recuperação (busca) + geração (LLM).
- **Frontend (TypeScript)**: interface para conversar/testar as perguntas e respostas.

Linguagens predominantes no repo: **TypeScript** e **Python**. :contentReference[oaicite:2]{index=2}

---

## Requisitos

- **Python 3.10+** (recomendado)
- **Node.js 18+** (recomendado)
- `pip` e `npm`
