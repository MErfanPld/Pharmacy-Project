from django.urls import path
from .views import (
    DrugListView, DrugDetailView, AddToOrderView, OrderSummaryView, PaymentView
)

urlpatterns = [
    path('drugs/', DrugListView.as_view(), name='drug-list'),  # لیست داروها
    path('drugs/<int:pk>/', DrugDetailView.as_view(), name='drug-detail'),  # جزئیات دارو
    path('add-to-order/', AddToOrderView.as_view(), name='add-to-order'),  # اضافه کردن به سفارش
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),  # خلاصه سفارش
    path('payment/', PaymentView.as_view(), name='payment'),  # پرداخت
]
