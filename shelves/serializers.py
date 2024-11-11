from rest_framework import serializers
from .models import Shelf, LocationShelf


class LocationShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationShelf
        fields = ['id', 'name', 'status', 'created_at', 'updated_at']


class ShelfSerializer(serializers.ModelSerializer):
    location_ids = serializers.PrimaryKeyRelatedField(
        queryset=LocationShelf.objects.all(),
        many=True,
        write_only=True
    )
    location = serializers.SerializerMethodField()

    class Meta:
        model = Shelf
        fields = ['id', 'name', 'location', 'location_ids', 'capacity',
                  'status', 'created_at', 'updated_at', 'is_full']
        read_only_fields = ['is_full']

    def get_location(self, obj):
        return [loc.name for loc in obj.location.all()]

    def create(self, validated_data):
        locations = validated_data.pop('location_ids', [])
        shelf = Shelf.objects.create(**validated_data)
        shelf.location.set(locations)
        return shelf

    def update(self, instance, validated_data):
        locations = validated_data.pop('location_ids', [])
        instance.name = validated_data.get('name', instance.name)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if locations:
            instance.location.set(locations)

        return instance
