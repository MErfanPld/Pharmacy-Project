from django.contrib import admin
from .models import Shelf
# Register your models here.

@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'capacity', 'jcreated', 'status']
    search_fields = ('name', 'capacity', 'status')