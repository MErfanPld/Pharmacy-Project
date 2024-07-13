from django.contrib import admin
from .models import CategoryDrug,Drug

# Register your models here.
@admin.register(CategoryDrug)
class CategoryDrugAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'jcreated']
    search_fields = ('name', 'status')


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','price', 'quantity','expiration_date','status', 'jcreated']
    search_fields = ('name', 'price', 'status')


