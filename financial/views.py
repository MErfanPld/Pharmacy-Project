from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .models import Transaction, FinancialReport
from .serializers import TransactionSerializer, FinancialReportSerializer


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class FinancialReportCreateAPIView(generics.ListCreateAPIView):
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer


class FinancialReportDetailAPIView(generics.ListCreateAPIView):
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer
