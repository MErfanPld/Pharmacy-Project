from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShelfViewSet

router = DefaultRouter()
router.register(r'shelves', ShelfViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
