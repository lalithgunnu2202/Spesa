from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    prods = Product.objects.all()
    cats = Type.objects.all()
    return render(request,'homepage.html',{'prods':prods,'cats':cats})