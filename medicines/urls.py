from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('', DrugListView.as_view(), name='drug-list'),
    path('create/', DrugCreateView.as_view(), name='drug-create'),
    path('update/<int:pk>/', DrugUpdateView.as_view(), name='drug-update'),
    path('delete/<int:pk>/', DrugDeleteView.as_view(), name='drug-delete'),
    
    path('category/', CategoryDrugListView.as_view(), name='category-drug-list'),
    path('category/create/', CategoryDrugCreateView.as_view(), name='category-drug-create'),
    path('category/update/<int:pk>/', CategoryDrugUpdateView.as_view(), name='category-drug-update'),
    path('category/delete/<int:pk>/', CategoryDrugDeleteView.as_view(), name='category-drug-delete'),
]

urlpatterns += dashboard_urls
