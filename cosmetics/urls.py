from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CosmeticItemViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'cosmetics', CosmeticItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
