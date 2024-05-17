from django.contrib import admin
from django.urls import path
from . import views
from .views import HomeView, MissionView, AddMissionView, BlogSearchView

urlpatterns = [
     path('', views.signin, name="signin"),  # Added trailing slash
    path('missions/<int:pk>', MissionView.as_view(), name='mission-details'),
    path('index/', HomeView.as_view(), name="LandingPage"),
    path('mission_post/', AddMissionView.as_view(), name="add-mission"),
    path('index/', views.BlogSearchView.as_view(), name='search_blogs'),
    path('signup/', views.signup, name="signup"),  # Added trailing slash
    path('signin/', views.signin, name="signin"),  # Added trailing slash
    path('signout/', views.signout, name="signout"),  # Added trailing slash
    path('about/', views.about, name="about"),
    path('contact_us/', views.contact_us, name="contact_us"),
]
