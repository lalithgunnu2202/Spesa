from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/<str:cat_name>', views.specific_view, name='specific_view'),
    path('all_products/',views.all_view,name='all_products'),
]