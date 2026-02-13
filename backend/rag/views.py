from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rag.chat import responder

@csrf_exempt
@api_view(["POST"])
def chat(request):
    message = request.data.get("message")

    if not message:
        return Response(
            {"error": "Field 'message' is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    resposta = responder(message)

    return Response({
        "response": resposta,
        "produtos_relacionados": []
    })

