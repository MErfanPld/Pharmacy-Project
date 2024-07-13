from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('', InsuranceListView.as_view(), name='insurance-list'),
    path('create/', InsuranceCreateView.as_view(), name='insurance-create'),
    path('update/<int:pk>/', InsuranceUpdateView.as_view(), name='insurance-update'),
    path('delete/<int:pk>/', InsuranceDeleteView.as_view(), name='insurance-delete'),
]

urlpatterns += dashboard_urls
