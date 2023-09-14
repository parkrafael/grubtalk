from django.contrib import admin
from django.urls import path

from . import views

app_name = "profile"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register_request, name = 'register'),
    path('login/', views.login_request, name = 'login'),
]
