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

    def get_user_permissions(self, obj):
        user_permissions = UserPermission.objects.filter(user=obj)
        return UserPermissionSerializer(user_permissions, many=True).data
