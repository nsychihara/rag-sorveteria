import os
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI

from rag.busca import buscar_produtos_semantico

logger = logging.getLogger(__name__)

MAX_MESSAGE_LENGTH = 1000
GROK_TIMEOUT = 30
GROK_MODEL = "grok-beta"


def get_openai_client():
    api_key = os.getenv("GROK_API_KEY")
    if not api_key:
        raise ValueError("GROK_API_KEY not configured")
    return OpenAI(api_key=api_key, base_url="https://api.x.ai/v1", timeout=GROK_TIMEOUT)


class Chatbot(APIView):
    def post(self, request):
        mensagem_usuario = self._extrair_mensagem(request)
        if mensagem_usuario is None:
            return Response(
                {"error": "Campo 'message' é obrigatório e não pode estar vazio"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if len(mensagem_usuario) > MAX_MESSAGE_LENGTH:
            return Response(
                {"error": f"Mensagem excede o limite de {MAX_MESSAGE_LENGTH} caracteres"},
                status=status.HTTP_400_BAD_REQUEST
            )

        produtos_relevantes = self._recuperar_contexto(mensagem_usuario)
        resposta_chatbot = self._gerar_resposta(mensagem_usuario, produtos_relevantes)

        return Response(
            {
                "response": resposta_chatbot,
                "produtos_relacionados": produtos_relevantes
            },
            status=status.HTTP_200_OK
        )

    def _extrair_mensagem(self, request):
        mensagem = request.data.get("message", "").strip()
        if not mensagem:
            return None
        return mensagem

    def _recuperar_contexto(self, mensagem: str):
        try:
            produtos = buscar_produtos_semantico(mensagem, top_k=5)
            return produtos
        except Exception as e:
            logger.error(f"Erro ao recuperar contexto: {type(e).__name__}")
            return []

    def _gerar_resposta(self, mensagem: str, produtos: list):
        contexto = self._formatar_contexto(produtos)

        prompt = f"""Você é um assistente virtual de uma sorveteria.
Sua função é ajudar os clientes de forma amigável e prestativa.

Informações dos produtos disponíveis:
{contexto}

Pergunta do cliente: {mensagem}

Responda de forma natural, amigável e útil. Se os produtos recuperados forem relevantes para a pergunta,
mencione-os naturalmente na resposta. Se não houver produtos relevantes ou a pergunta for sobre horário,
localização ou outros assuntos, responda de forma adequada mesmo sem mencionar produtos específicos."""

        try:
            client = get_openai_client()
            response = client.chat.completions.create(
                model=GROK_MODEL,
                messages=[
                    {"role": "system", "content": "Você é um assistente virtual de uma sorveteria. Sua função é ajudar os clientes de forma amigável e prestativa."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Erro ao gerar resposta: {type(e).__name__}")
            return "Desculpe, não consegui processar sua mensagem no momento. Por favor, tente novamente."

    def _formatar_contexto(self, produtos: list):
        if not produtos:
            return "Nenhum produto específico encontrado para esta consulta."

        contexto_texto = ""
        for i, produto in enumerate(produtos, 1):
            contexto_texto += f"{i}. {produto['nome']}\n"
            contexto_texto += f"   Descrição: {produto['descricao']}\n"
            contexto_texto += f"   Relevância: {produto['score']:.2f}\n\n"

        return contexto_texto
