from django.urls import path

from users.views import UserLoginAPIView

urlpatterns = [
   path('login/', UserLoginAPIView.as_view(), name='login'),
]
