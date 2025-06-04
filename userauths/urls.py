from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('signup/', views.signup_view , name='signup'),
    path('userlogin/', views.login_view , name='login'),
    path('userreset/', views.reset_view , name='resetpassword'),
]