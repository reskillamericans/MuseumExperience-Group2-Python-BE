"""museumadmin URL Configuration

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
from django.urls import path, include
from adminapp import views as adminapp_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adminapp_views.index, name="Homepage" ),
    #path('adminapp/', include('adminapp.urls')),
    path('register/', adminapp_views.register, name='register'),
    path('register/visitor/', adminapp_views.visitor_register.as_view(success_url="/"), name='visitor_register'),
    path('register/staff/', adminapp_views.staff_register.as_view(success_url="/"), name='staff_register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
] 