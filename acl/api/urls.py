from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = "acl"

router = SimpleRouter()
# router.register('roles', views.RoleAPI)
router.register('permissions', views.PermissionsAPI)
# router.register(r'user-permissions', views.UserPermissionViewSet)
# router.register('role_user', views.UserRoleAPI)

urlpatterns = [
    # path('', include(router.urls)),
    path('user-permissions/', views.UserPermissionListCreateView.as_view(), name='user-permissions-list-create'),
    path('user-permissions/<int:pk>/', views.UserPermissionDetailView.as_view(), name='user-permissions-detail'),

]