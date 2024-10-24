from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from acl.api.serializer import UserPermissionSerializer
from acl.models import UserPermission
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    user_permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_user_permissions(self, obj):
        user_permissions = UserPermission.objects.filter(user=obj)
        return UserPermissionSerializer(user_permissions, many=True).data


    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phoneNumber=validated_data['phoneNumber'],
            national_id=validated_data['national_id'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
