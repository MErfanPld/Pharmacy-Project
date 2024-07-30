from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListAPIView.as_view(), name="user-list-api"),
    path('create/', UserCreateAPIView.as_view(), name="user-create-api"),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name="user-update-api"),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name="user-delete-api"),
]