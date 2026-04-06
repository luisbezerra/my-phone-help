from django.urls import path
from .views import HardwareLoginAPIView

urlpatterns = [
    path('login-hwid/', HardwareLoginAPIView.as_view(), name='api_login_hwid'),
]
