from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'is_paid']
    search_fields = ('user', 'is_paid')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'drug', 'quantity', 'price']
    search_fields = ('order', 'drug', 'quantity', 'price')
