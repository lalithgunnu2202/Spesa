from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/',views.delete_from_cart, name='delete_from_cart')
]