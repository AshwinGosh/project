from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
   path('', views.house,name='house'),
   path('home/', views.home,name='home'),
   path('login/', views.login,name='login'),
   path('register/', views.register,name='register'),
   path('feedback/', views.feedback_home,name='feedback'),
   path("announcements/", views.announcements_page, name="announcements_page"),
]