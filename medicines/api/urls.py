from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'category-drugs', CategoryDrugViewSet)
router.register(r'drugs', DrugViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/low-stock-report/', LowStockReportView.as_view(), name='low_stock_report'),
]
