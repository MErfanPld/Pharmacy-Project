from django.db import models

from extenstions.utils import jalali_converter

# Create your models here.

class LocationShelf(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام")
    status = models.BooleanField(default=False, verbose_name="وضعیت")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="تاریخ بروزرسانی")

    def __str__(self):
        return self.name

    @property
    def get_status(self):
        return 'تایید شده' if self.status else 'تایید نشده'

    def jcreated(self):
        return jalali_converter(self.created_at)

    class Meta:
        verbose_name = 'موفعیت قفسه'
        verbose_name_plural = 'موفعیت قفسه ها'

class Shelf(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام")
    location = models.ManyToManyField(LocationShelf, related_name='shelfs', verbose_name="موقعیت")  
    capacity = models.IntegerField(verbose_name="تعداد")
    status = models.BooleanField(default=False, verbose_name="وضعیت")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="تاریخ بروزرسانی")

    def __str__(self):
        return self.name

    @property
    def get_status(self):
        return 'تایید شده' if self.status else 'تایید نشده'

    def jcreated(self):
        return jalali_converter(self.created_at)

    class Meta:
        verbose_name = 'قفسه'
        verbose_name_plural = 'قفسه ها'
