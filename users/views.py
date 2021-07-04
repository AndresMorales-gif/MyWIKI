from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import UserLoginSerializer
from users.serializers import UserModelSerializer
class UserLoginAPIView(APIView):
    

    def post(self, request):
        serializers = UserLoginSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user, token = serializers.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)