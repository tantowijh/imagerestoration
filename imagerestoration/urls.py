"""
URL configuration for imagerestoration project.

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
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings
from .utils import cleanup_media_and_redirect

urlpatterns = [
    path('configuration/', include('configuration.urls')),
    path('cleanup/<str:redirect_url_name>/', cleanup_media_and_redirect, name='cleanup_media_and_redirect'),
    path('restoration/', include('restoration.urls')),
    path('enhancement/', include('enhancement.urls')),
    path('denoising/', include('denoising.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', lambda request: redirect('restoration:index')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
