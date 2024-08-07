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
    class Meta:
        model = UserPermission
        fields = '__all__'
