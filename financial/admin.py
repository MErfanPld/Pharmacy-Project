from django.contrib import admin
from .models import Transaction, FinancialReport

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'amount', 'date', 'total_amount')
    list_filter = ('transaction_type', 'date')
    search_fields = ('description',)

@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'total_income', 'total_expense', 'net_balance')
    search_fields = ('start_date', 'end_date')
