"""
URL configuration for villa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from villApp import views
from django .conf.urls.static import static
from django .conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index,name='index'),
    path('regis/', views.regis, name='regis'),
    path("login/", views.login,name='login'),
    path("userdtl", views.userdtl,name='userdtl'),
    path("contact/", views.contact,name='contact'),
    path("why/", views.why,name='why'),
    path("testimonial/", views.testimonial,name='testimonial'),
    path("", views.upload_image, name='upload_image'),
    path('delete_image/<int:id>/', views.delete_image, name='delete_image'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)