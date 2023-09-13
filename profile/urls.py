from django.contrib import admin
from django.urls import path

from . import views

app_name = "profile"

urlpatterns = [
    # root page
    path('', views.index, name = 'index'),
    # register page
    path('register/', views.register_request, name = 'register'),
    # login page
    path('login/', views.login_request, name = 'login'),
]
