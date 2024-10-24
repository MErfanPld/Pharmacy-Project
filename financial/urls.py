from django.urls import path
from .views import TransactionListCreateAPIView, TransactionDetailAPIView, FinancialReportCreateAPIView, FinancialReportDetailAPIView

urlpatterns = [
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction-detail'),

    path('reports/', FinancialReportCreateAPIView.as_view(), name='financial-report-create'),
    path('reports/<int:pk>/', FinancialReportDetailAPIView.as_view(), name='financial-report-detail'),
]
