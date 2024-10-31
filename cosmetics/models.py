from shelves.models import *
from django.db import models

from extenstions.utils import jalali_converter

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام دسته")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'


class CosmeticItem(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="نام محصول")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cosmetics', verbose_name="دسته بندی")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    shelf = models.ForeignKey(Shelf, blank=True,null=True,on_delete=models.CASCADE, related_name='cosmetics', verbose_name="قفسه")
    code_item = models.CharField(max_length=255,blank=True,null=True ,unique=True,
                            verbose_name="کد محصول")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    quantity = models.IntegerField(verbose_name="تعداد موجود")
    manufacturer = models.CharField(max_length=255, verbose_name="تولید کننده")
    expiration_date = models.DateField(verbose_name="تاریخ انقضا", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    def __str__(self):
        return f"{self.name} | {self.category}"

    class Meta:
        verbose_name = 'محصول آرایشی و بهداشتی'
        verbose_name_plural = 'محصولات آرایشی و بهداشتی'

    def jexpiration_date(self):
        return self.expiration_date.replace('-', '/')
    
    def jcreated(self):
        return jalali_converter(self.created_at)