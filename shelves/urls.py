from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShelfViewSet, LocationShelfListAPIView, LocationShelfCreateAPIView, LocationShelfUpdateAPIView, LocationShelfDestroyAPIView

router = DefaultRouter()
router.register(r'shelves', ShelfViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/location/', LocationShelfListAPIView.as_view(), name="location-list-api"),
    path('api/location/create/', LocationShelfCreateAPIView.as_view(), name="location-create-api"),
    path('api/location/update/<int:pk>/', LocationShelfUpdateAPIView.as_view(), name="location-update-api"),
    path('api/location/delete/<int:pk>/', LocationShelfDestroyAPIView.as_view(), name="location-delete-api"),
]
