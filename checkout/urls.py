from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('checkout/product/<int:item_id>',views.checkout_product_view,name='checkout_page'),
    path('checkout/cart/',views.checkout_cart_view,name='checkout_cart'),
]