from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "profile"

urlpatterns = [
    # homepage
    path('', views.index, name = 'index'),
    # register page
    path('register/', views.register_request, name = 'register'),
    # login page
    path('login/', views.login_request, name = 'login'),
]
