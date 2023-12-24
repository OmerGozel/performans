"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, re_path, path

from django.urls import re_path as url

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'',include('profiller.api.urls')),
    re_path(r'api-auth/',include('rest_framework.urls')),#Browsable api sayfasi icin
    re_path(r'api/rest-auth/',include('rest_auth.urls')), #django-rest-auth ile gelen endpointler icin
    re_path(r'api/rest-auth/registration/',include('rest_auth.registration.urls')), #django-rest-auth ile gelen endpointler icin
    re_path(r'api/',include('profiller.api.urls')),
#      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#      path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)