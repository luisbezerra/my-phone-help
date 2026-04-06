from rest_framework import viewsets
from .serializers import BrandSerializer
from .models import Brand

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.filter(is_active=True)
    serializer_class = BrandSerializer
