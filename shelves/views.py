from django.shortcuts import render
from rest_framework import viewsets
from .models import Shelf
from .serializers import ShelfSerializer

# Create your views here.

class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
