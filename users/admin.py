from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Users


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name')


# Register your models here.
admin.site.register(Users, CustomUserAdmin)
