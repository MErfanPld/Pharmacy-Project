from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderItemListView.as_view(), name='order-list'),
    # path('update/<int:pk>/', views.OrderAdminUpdateView.as_view(), name='order-update'),
    path('delete/<int:pk>/', views.OrderAdminDeleteView.as_view(), name='order-delete'),
    
    path('drugs/', views.drug_list, name='drug_list'),
    path('drugs/<int:pk>/', views.drug_detail, name='drug_detail'),
    path('order/add/', views.add_to_order, name='add_to_order'),
    path('order/', views.order_summary, name='order_summary'),
    path('payment/', views.payment, name='payment'),
]
