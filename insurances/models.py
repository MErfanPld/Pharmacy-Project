from django.db import models

from extenstions.utils import jalali_converter


# Create your models here.

class Insurance(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام بیمه")
    price = models.FloatField(verbose_name="درصد تخفیف")
    status = models.BooleanField(default=False, verbose_name="وضعیت")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )

    def __str__(self):
        return f"{self.name} | {self.status} "

    class Meta:
        verbose_name = 'بیمه'
        verbose_name_plural = 'بیمه ها'

    @property
    def get_status(self):
        return 'تایید شده' if self.status else 'تایید نشده'

    def jcreated(self):
        return jalali_converter(self.created_at)
