from rest_framework import serializers
from ..models import CategoryDrug, Drug


class CategoryDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDrug
        fields = '__all__'


class DrugSerializer(serializers.ModelSerializer):
    interactions = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Drug
        fields = "__all__"
