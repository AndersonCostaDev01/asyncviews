from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', views.timer, name='timer'),
    path('async_view/', views.async_view, name='async_view'),
    path('sync_view/', views.sync_view, name='sync_view'),
    path('', views.home),
]
