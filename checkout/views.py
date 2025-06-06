from django.shortcuts import render, get_object_or_404
from home.models import *
from cart.models import Cart_item
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def checkout_product_view(request,item_id):
    item = get_object_or_404(Product,id=item_id)
    return render(request,'product_checkout/checkout.html',{'item':item})

@login_required
def checkout_cart_view(request):
    cart = Cart_item.objects.filter(user=request.user)
    total_price = sum(item.product.price for item in cart)
    return render(request,'cart_checkout/checkout.html',{'cart':cart,'total':total_price})

@login_required
def order_confirmed(request):
    return render(request,'orderconfirmed.html')