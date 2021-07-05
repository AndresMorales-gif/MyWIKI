from users.serializers.UserModelSerializer import UserModelSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers.UserSignUpSerializer import UserSignUpSerializer


class UserSignUpAPIView(APIView):

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
