from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryDrugViewSet, DrugViewSet

router = DefaultRouter()
router.register(r'category-drugs', CategoryDrugViewSet)
router.register(r'drugs', DrugViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
