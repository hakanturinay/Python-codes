from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from . import views

app_name = "user" 
urlpatterns = [
    path('register/', views.register,name = "register"),
    path('login/', views.loginUser,name = "login"),
    path('logout/', views.logoutUser,name = "logout"),
]