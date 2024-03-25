from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('tickit.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
    ]