from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(
            username=data['email'].lower(),
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError(
                'The account has not been verified.'
            )
        self.context['user'] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
