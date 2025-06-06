from django.shortcuts import render
from .models import *
# from cart.models import Cart_item
# from django.contrib.auth.models import User
# Create your views here.
def index(request):
    prods = Product.objects.all()[:4]
    eight_prods = Product.objects.all()[:8]
    cats = Type.objects.all()
    # count = Cart_item.objects.filter(user=request.user).count()
    return render(request,'homepage.html',{'prods':prods,'cats':cats,'eight_prods':eight_prods})