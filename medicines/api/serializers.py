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
        
    def validate_name(self, value):
        if Drug.objects.filter(name=value).exists():
            raise serializers.ValidationError("این دارو قبلاً ثبت شده است.")
        return value
