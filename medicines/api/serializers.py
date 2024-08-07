from rest_framework import serializers
from ..models import CategoryDrug, Drug

class CategoryDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDrug
        fields = '__all__'

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'
