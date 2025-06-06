from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('product/<int:item_id>',views.view_product,name='product_details'),
]