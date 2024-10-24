from rest_framework import serializers
from .models import Transaction, FinancialReport

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'amount', 'description', 'tax', 'total_amount', 'date']
        read_only_fields = ['total_amount', 'date']

class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = ['id', 'start_date', 'end_date', 'total_income', 'total_expense', 'net_balance']
        read_only_fields = ['total_income', 'total_expense', 'net_balance']
