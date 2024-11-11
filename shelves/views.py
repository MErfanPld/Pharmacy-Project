from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from acl.rest_mixin import RestPermissionMixin
from .models import Shelf, LocationShelf
from .serializers import ShelfSerializer, LocationShelfSerializer

# Create your views here.

# class ShelfViewSet(viewsets.ModelViewSet):
#     queryset = Shelf.objects.all()
#     serializer_class = ShelfSerializer


class ShelfListCreateAPIView(ListCreateAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

class ShelfDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class LocationShelfListAPIView(APIView):
    permission_classes = [RestPermissionMixin]

    def get(self, request):
        location_shelves = LocationShelf.objects.all()
        serializer = LocationShelfSerializer(location_shelves, many=True)
        return Response(serializer.data)

class LocationShelfCreateAPIView(CreateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['LocationShelf_create']
    queryset = LocationShelf.objects.all()
    serializer_class = LocationShelfSerializer


class LocationShelfUpdateAPIView(UpdateAPIView):
    queryset = LocationShelf.objects.all()
    serializer_class = LocationShelfSerializer
    permission_classes = [RestPermissionMixin] 

class LocationShelfDestroyAPIView(DestroyAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['LocationShelf_delete']
    queryset = LocationShelf.objects.all()
    serializer_class = LocationShelfSerializer
