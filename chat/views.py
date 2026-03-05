from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import ChatMessage
from ai_engine.chatbot import generate_chat_response


class ChatAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        user_message = request.data.get("message")

        ai_response = generate_chat_response(user_message)

        chat = ChatMessage.objects.create(
            user=request.user,
            message=user_message,
            response=ai_response
        )

        return Response({
            "message": chat.message,
            "response": chat.response
        })