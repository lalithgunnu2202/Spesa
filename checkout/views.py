from django.shortcuts import render, get_object_or_404
from home.models import *
from cart.models import Cart_item
from django.contrib.auth.models import User

# Create your views here.
def checkout_product_view(request,item_id):
    item = get_object_or_404(Product,id=item_id)
    return render(request,'product_checkout/checkout.html',{'item':item})

def checkout_cart_view(request):
    cart = Cart_item.objects.filter(user=request.user)
    total_price = sum(item.product.price for item in cart)
    return render(request,'cart_checkout/checkout.html',{'cart':cart,'total':total_price})