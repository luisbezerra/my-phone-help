from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet

router = DefaultRouter()
router.register(r'marcas', BrandViewSet) # Note que aqui NÃO tem barra

urlpatterns = [
    path('', include(router.urls)), # O router já cria os caminhos
]
