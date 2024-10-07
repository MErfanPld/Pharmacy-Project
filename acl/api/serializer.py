from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import *


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class Role_UserSerializer(ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'
        depth = 1


class UserPermissionSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(), many=True)
    
    permissions_display = serializers.SerializerMethodField()

    class Meta:
        model = UserPermission
        fields = ['user', 'permissions', 'permissions_display']

    def get_permissions_display(self, obj):
        return [perm.name for perm in obj.permissions.all()]

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions')
        user_permission = UserPermission.objects.create(**validated_data)
        user_permission.permission.set(permissions_data)
        return user_permission

    def update(self, instance, validated_data):
        permissions_data = validated_data.pop('permissions', None)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        if permissions_data is not None:
            instance.permissions.set(permissions_data)
        return instance