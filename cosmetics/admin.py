from django.contrib import admin
from .models import Category, CosmeticItem

class CosmeticItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'manufacturer', 'expiration_date', 'jcreated')
    list_filter = ('category', 'manufacturer', 'expiration_date')
    search_fields = ('name', 'manufacturer')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(CosmeticItem, CosmeticItemAdmin)
