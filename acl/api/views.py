from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import *
from .serializer import *

# Create your views here.


class RoleAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PermissionsAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class UserPermissionViewSet(ModelViewSet):
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer
    permission_classes = [IsAuthenticated]


class UserRoleAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserRole.objects.all()
    serializer_class = Role_UserSerializer
