from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rag.chat import responder


@api_view(["POST"])
def chat(request):
    pergunta = request.data.get("pergunta")

    if not pergunta:
        return Response(
            {"erro": "Campo 'pergunta' é obrigatório."},
            status=status.HTTP_400_BAD_REQUEST
        )

    resposta = responder(pergunta)

    return Response({"resposta": resposta})
