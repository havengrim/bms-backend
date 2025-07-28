from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,      # for login - get access and refresh tokens
    TokenRefreshView,         # for refreshing access token
)
from .views import register
urlpatterns = [
    path('register/', register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]