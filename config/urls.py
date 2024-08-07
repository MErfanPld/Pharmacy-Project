"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView,SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('dashboard/users/', include('users.urls')),
    path('dashboard/accounts/', include('accounts.urls')),
    path('dashboard/insurances/', include('insurances.urls')),
    path('dashboard/medicines/', include('medicines.urls')),
    path('dashboard/orders/', include('orders.urls')),
    path('dashboard/chats/', include('chats.urls')),
    path('dashboard/acl/', include('acl.urls')),
]

urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/users/', include('users.api.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/acl/', include('acl.api.urls')),
    path('api/medicines/', include('medicines.api.urls')),
    # path('api/insurances/', include('insurances.api.urls')),
    # path('api/orders/', include('orders.api.urls')),
    # path('api/chats/', include('chats.api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)