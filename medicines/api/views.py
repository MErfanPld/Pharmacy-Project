from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from ..models import CategoryDrug, Drug
from .serializers import CategoryDrugSerializer, DrugSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import HasCategoryDrugPermissions, HasDrugPermissions


class CategoryDrugViewSet(viewsets.ModelViewSet):
    queryset = CategoryDrug.objects.all()
    serializer_class = CategoryDrugSerializer
    permission_classes = [permissions.IsAuthenticated, HasCategoryDrugPermissions]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [permissions.IsAuthenticated, HasDrugPermissions]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'