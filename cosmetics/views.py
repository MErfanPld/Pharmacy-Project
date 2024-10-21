from rest_framework import viewsets
from .models import Category, CosmeticItem
from .serializers import CategorySerializer, CosmeticItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CosmeticItemViewSet(viewsets.ModelViewSet):
    queryset = CosmeticItem.objects.all()
    serializer_class = CosmeticItemSerializer
