from django.db import models
from django.conf import settings
from medicines.models import Drug
from extenstions.utils import jalali_converter


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده؟")

    def __str__(self):
        return f"{self.user.full_name} | وضعیت {self.get_is_paid}"

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    def jcreated(self):
        return jalali_converter(self.created_at)
    
    @property
    def get_is_paid(self):
        return 'پرداخت شده' if self.is_paid else 'پرداخت نشده'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    drug = models.ForeignKey(
        Drug, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(verbose_name="تعداد")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )

    def __str__(self):
        return f"{self.quantity} x {self.drug.name}"

    class Meta:
        verbose_name = 'موارد سفارش'
        verbose_name_plural = 'موارد سفارش ها'

    def jcreated(self):
        return jalali_converter(self.created_at)
