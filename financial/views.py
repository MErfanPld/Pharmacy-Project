from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Transaction, FinancialReport
from .serializers import TransactionSerializer, FinancialReportSerializer


class TransactionListCreateAPIView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({'error': 'تراکنش پیدا نشد'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({'error': 'تراکنش پیدا نشد'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({'error': 'تراکنش پیدا نشد'}, status=status.HTTP_404_NOT_FOUND)

        transaction.delete()
        return Response({'message': 'تراکنش با موفقیت حذف شد'}, status=status.HTTP_204_NO_CONTENT)


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
