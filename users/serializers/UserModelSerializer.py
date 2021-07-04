from django.db import models
from django.db.models import fields
from rest_framework import serializers

from users.models import Users

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )