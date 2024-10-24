from django.db import models
from django.utils import timezone


class BaseFinancialModel(models.Model):
    description = models.TextField(
        blank=True, null=True, verbose_name='توضیحات')
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ')

    class Meta:
        abstract = True


class Transaction(BaseFinancialModel):
    TRANSACTION_TYPE = [
        ('income', 'دریافتی'),
        ('expense', 'برداشت'),
    ]
    transaction_type = models.CharField(
        max_length=7, choices=TRANSACTION_TYPE, verbose_name='نوع تراکنش')
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='مبلغ')
    tax = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0, verbose_name='مالیات (%)')
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, verbose_name='مبلغ کل')

    def save(self, *args, **kwargs):
        self.total_amount = self.amount + (self.amount * (self.tax / 100))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_transaction_type_display()} - {self.amount}'

    class Meta:
        verbose_name = 'تراکنش'
        verbose_name_plural = 'تراکنش‌ها'


class FinancialReport(models.Model):
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان')
    total_income = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, verbose_name='کل دریافتی‌ها')
    total_expense = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, verbose_name='کل برداشت‌ها')
    net_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, verbose_name='بالانس نهایی')

    def generate_report(self):
        transactions = Transaction.objects.filter(
            date__range=[self.start_date, self.end_date])
        self.total_income = transactions.filter(transaction_type='income').aggregate(
            models.Sum('total_amount'))['total_amount__sum'] or 0.0
        self.total_expense = transactions.filter(transaction_type='expense').aggregate(
            models.Sum('total_amount'))['total_amount__sum'] or 0.0
        self.net_balance = self.total_income - self.total_expense
        self.save()

    def __str__(self):
        return f'گزارش مالی از {self.start_date} تا {self.end_date}'

    class Meta:
        verbose_name = 'گزارش مالی'
        verbose_name_plural = 'گزارش‌های مالی'
