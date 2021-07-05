from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.models import WikiModel
# Create your models here.


class Users(WikiModel, AbstractUser):

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user already exists with mail.'
        }
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_verified = models.BooleanField(
        'verified',
        default=False
    )

    def __str__(self):
        return self.username
