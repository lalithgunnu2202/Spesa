from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart_item 
from home.models import Product
from django.contrib import messages

# Create your views here.
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item , created = Cart_item.objects.get_or_create(user = request.user, product = product)
    if not created:
        messages.info(request,"Product is already in the Cart")
        cart_item.save()
        return redirect('view_cart')
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = Cart_item.objects.filter(user=request.user).select_related('product')
    sub_total = sum(item.product.price for item in cart_items)
    return render(request,'cart.html',{'cart_items':cart_items,'sub_total':sub_total,'total_price':sub_total+9.99})

@login_required
def delete_from_cart(request, item_id):
    product = get_object_or_404(Product, id=item_id)
    cart_item = get_object_or_404(Cart_item, user=request.user, product=product)
    cart_item.delete()
    return redirect('view_cart')
