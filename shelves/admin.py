from django.contrib import admin
from .models import Shelf, LocationShelf
# Register your models here.

@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_location', 'capacity', 'jcreated', 'status']
    search_fields = ('name', 'capacity')

    def get_location(self, obj):
        return ", ".join([loc.name for loc in obj.location.all()])
    get_location.short_description = 'موقعیت'

@admin.register(LocationShelf)
class LocationShelfAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'jcreated', 'status']
    search_fields = ('name', 'status')
