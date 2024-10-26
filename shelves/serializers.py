from rest_framework import serializers
from .models import Shelf, LocationShelf


class LocationShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationShelf
        fields = ['id', 'name', 'status', 'created_at', 'updated_at']


class ShelfSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField(
        read_only=True, source='location.name')

    class Meta:
        model = Shelf
        fields = ['id', 'name', 'location',
                  'capacity', 'created_at', 'updated_at']

    def get_location(self, obj):
        return [loc.name for loc in obj.location.all()]
