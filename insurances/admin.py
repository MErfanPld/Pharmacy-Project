from django.contrib import admin
from .models import Insurance


# Register your models here.

@admin.register(Insurance)
class MedicalTestAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status', 'created_at']
    search_fields = ('name', 'price', 'status')
