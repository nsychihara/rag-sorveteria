import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def gerar_resposta(pergunta: str, contexto: str) -> str:

    prompt = f"""
Você é um atendente da Sorveteria.

Responda APENAS com base no contexto.
Não invente produtos.
Use apenas as informações abaixo para responder.

Contexto:
{contexto}

Pergunta:
{pergunta}

Se a resposta não estiver no contexto, diga que não encontrou a informação.
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return completion.choices[0].message.content
