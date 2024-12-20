from shelves.models import *
from django.db import models
from extenstions.utils import jalali_converter
from django_jalali.db.models import jDateField

# Create your models here.


class CategoryDrug(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name="نام دسته بندی")
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
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    @property
    def get_status(self):
        return 'تایید شده' if self.status else 'تایید نشده'

    def jcreated(self):
        return jalali_converter(self.created_at)


class Drug(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name="نام دارو")
    category = models.ForeignKey(
        CategoryDrug, on_delete=models.CASCADE, related_name='drugs', verbose_name="دسته بندی")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE,
                            related_name='drugs', verbose_name="قفسه", blank=True, null=True)
    code_drug = models.CharField(
        max_length=255, blank=True, null=True, unique=True, verbose_name="کد دارو")
    interactions = models.ManyToManyField(
        'self', blank=True, symmetrical=False, verbose_name="تداخل‌های دارویی")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت")
    quantity = models.IntegerField(verbose_name="تعداد")
    manufacturer = models.CharField(max_length=255, verbose_name="تولید کننده")
    expiration_date = models.CharField(
        verbose_name="تاریخ انقضا", max_length=255)
    status = models.BooleanField(default=False, verbose_name="وضعیت")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return f"{self.name} | {self.category}"

    class Meta:
        verbose_name = 'دارو'
        verbose_name_plural = 'دارو ها'

    @property
    def get_status(self):
        return 'تایید شده' if self.status else 'تایید نشده'

    def jcreated(self):
        return jalali_converter(self.created_at)

    def jexpiration_date(self):
        return self.expiration_date.replace('-', '/')
