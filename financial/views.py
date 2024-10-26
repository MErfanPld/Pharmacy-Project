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

class FinancialReportCreateAPIView(APIView):
    def post(self, request):
        serializer = FinancialReportSerializer(data=request.data)
        if serializer.is_valid():
            report = serializer.save()
            report.generate_report()
            return Response(FinancialReportSerializer(report).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinancialReportDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            report = FinancialReport.objects.get(pk=pk)
        except FinancialReport.DoesNotExist:
            return Response({'error': 'گزارش مالی پیدا نشد'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FinancialReportSerializer(report)
        return Response(serializer.data)
