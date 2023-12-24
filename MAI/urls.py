"""MAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("api.urls")),
    path("", TemplateView.as_view(template_name='index.html')),
    path("product", TemplateView.as_view(template_name='index.html')),
    path("product/products-details", TemplateView.as_view(template_name='index.html')),
    path("who-we-are", TemplateView.as_view(template_name='index.html')),
    path("contact-us", TemplateView.as_view(template_name='index.html')),
    path("dashboard", TemplateView.as_view(template_name='index.html')),
    
    path("dashboard/login", TemplateView.as_view(template_name='index.html')),
    path("dashboard/add-products", TemplateView.as_view(template_name='index.html')),
    path("dashboard/update-products", TemplateView.as_view(template_name='index.html')),
    path("dashboard/latest-product", TemplateView.as_view(template_name='index.html')),
    path("dashboard/hot-product", TemplateView.as_view(template_name='index.html')),
    path("dashboard/drafts", TemplateView.as_view(template_name='index.html')),
    path("dashboard/deleted", TemplateView.as_view(template_name='index.html')),
    path("dashboard/inquiry", TemplateView.as_view(template_name='index.html')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.ASSETS_URL, document_root=settings.STATICFILES_DIRS[0])
