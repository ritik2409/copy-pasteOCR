from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from users.views import LoginAPIView, RegisterAPIView, EditAPIView

urlpatterns = [
    path('auth/login', LoginAPIView.as_view(), name="login"),
    path('auth/register', RegisterAPIView.as_view()),
    path('auth/jwt', obtain_jwt_token),
    path('auth/jwt/refresh', refresh_jwt_token),
]