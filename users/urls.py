from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('', UsersListView.as_view(), name='users-list'),
    path('create/', UsersCreateView.as_view(), name='users-create'),
    path('update/<int:pk>/', UsersUpdateView.as_view(), name='users-update'),
    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='users-delete'),
    path('change/password/<int:pk>/', UserChangePasswordView.as_view(), name='users-change-password'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('change/password/', ChangePasswordView.as_view(), name='change-password'),
    path('change/avatar/', ChangeAvatarView.as_view(), name='change-avatar'),

]

urlpatterns += dashboard_urls
