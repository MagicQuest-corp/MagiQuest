from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),  # Added trailing slash
    path('signin/', views.signin, name="signin"),  # Added trailing slash
    path('signout/', views.signout, name="signout"),  # Added trailing slash
]
