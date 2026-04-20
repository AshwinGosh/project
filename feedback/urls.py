from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
   path('', views.house,name='house'),
   path('home/', views.home,name='home'),
   path('login/', views.login,name='user_login'),
   path('register/', views.register,name='user_register'),

]