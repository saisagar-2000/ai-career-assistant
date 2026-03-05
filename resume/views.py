from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ResumeSerializer
from .services import process_resume


class ResumeUploadView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ResumeSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        resume = serializer.save(user=request.user)

        result = process_resume(resume)

        return Response(result)