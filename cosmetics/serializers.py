from rest_framework import serializers
from .models import Category, CosmeticItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CosmeticItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CosmeticItem
        fields = "__all__"
        
    def validate_name(self, value):
        if CosmeticItem.objects.filter(name=value).exists():
            raise serializers.ValidationError("این محصول قبلاً ثبت شده است.")
        return value
