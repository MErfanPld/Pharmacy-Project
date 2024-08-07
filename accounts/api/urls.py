from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

from . import views

app_name = "accounts"

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", views.UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
    path("users/", views.UserAPIView.as_view(), name="user-info"),
]