from rest_framework import serializers
from .models import Shelf

class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['id', 'name', 'location', 'capacity', 'created_at', 'updated_at']