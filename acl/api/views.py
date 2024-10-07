from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import *

from acl.permissions import PERMISSIONS, filter_permissions

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


class UserPermissionListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer

class UserPermissionDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer

class UserRoleAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserRole.objects.all()
    serializer_class = Role_UserSerializer
