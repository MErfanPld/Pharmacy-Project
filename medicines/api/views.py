from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from ..models import CategoryDrug, Drug
from .serializers import CategoryDrugSerializer, DrugSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import HasCategoryDrugPermissions, HasDrugPermissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryDrugViewSet(viewsets.ModelViewSet):
    queryset = CategoryDrug.objects.all()
    serializer_class = CategoryDrugSerializer
    permission_classes = [
        permissions.IsAuthenticated, HasCategoryDrugPermissions]


class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [permissions.IsAuthenticated, HasDrugPermissions]



class LowStockReportView(APIView):
    def get(self, request, *args, **kwargs):
        drugs = Drug.objects.all()
        low_stock_drugs = []

        for drug in drugs:
            stock_warning = drug.check_stock()
            if "کم است" in stock_warning:
                low_stock_drugs.append(drug)

        serializer = DrugSerializer(low_stock_drugs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
