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


class UpdateDrugStockView(APIView):
    def post(self, request, *args, **kwargs):
        drug_id = request.data.get('drug_id')
        shelf_quantity = request.data.get('shelf_quantity', 0)
        warehouse_quantity = request.data.get('warehouse_quantity', 0)

        try:
            drug = Drug.objects.get(id=drug_id)

            if drug.warehouse_quantity >= warehouse_quantity:
                drug.shelf_quantity += int(shelf_quantity)
                drug.warehouse_quantity -= int(shelf_quantity)
                drug.save()

                return Response({"message": "موجودی دارو بروز شد", "total_quantity": drug.total_quantity}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "موجودی انبار کافی نیست"}, status=status.HTTP_400_BAD_REQUEST)

        except Drug.DoesNotExist:
            return Response({"error": "دارو یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
