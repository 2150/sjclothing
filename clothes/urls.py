from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check_authentication/', views.check_authentication, name='check_authentication'),
    path('check_authentication/register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/login', views.login, name='login'),
    path('login/register', views.register, name='register'),
]