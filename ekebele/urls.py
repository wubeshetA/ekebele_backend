"""
URL configuration for ekebele project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from accounts.views import check_is_staff, VerifyEmailView
# import settings
from django.conf import settings
from django.conf.urls.static import static
from ekebele.admin import custom_admin_site


urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/', include('vital_events.urls')),
    path('auth/check-is-staff/', check_is_staff, name='check-is-staff'),
    path('auth/verify-email/', VerifyEmailView.as_view(), name='verify-email'),
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
