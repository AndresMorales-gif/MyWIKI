from django.contrib.auth import password_validation
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Users


class UserSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match")

        password_validation.validate_password(password)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        data['email'] = data['email'].lower()
        data['username'] = data['username'].lower()
        user = Users.objects.create_user(**data, is_verified=False)
        self.send_email(user)
        return user

    def send_email(self, data):
        token = self.get_token(data)
        subject = 'confirm your account'
        from_email = 'notification <notification@wiki.com>'
        content = render_to_string(
            'emails/email_verification.html',
            {'token': token, 'user': data}
        )
        email_message = EmailMultiAlternatives(
            subject,
            content,
            from_email,
            [data.email]
        )
        email_message.attach_alternative(content, "text/html")
        email_message.send()

    def get_token(self, data):
        return 'lasj'
