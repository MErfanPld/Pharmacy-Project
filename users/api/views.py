from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from acl.rest_mixin import RestPermissionMixin
from users.models import User
from users.api.serializers import *
from .serializers import UserSerializer

class UserListAPIView(ListAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['user_list']
    search_fields = ["title","slug"]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['user_create']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [RestPermissionMixin] 

class UserDestroyAPIView(DestroyAPIView):
    permission_classes = [RestPermissionMixin]
    permissions = ['user_delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer
