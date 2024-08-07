from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("is_superuser", "is_active", "is_staff")


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name","phoneNumber", "national_id","password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")