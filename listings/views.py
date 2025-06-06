from django.shortcuts import render, get_object_or_404
from home.models import *
# from django.core.paginator import Paginator

# Create your views here.
def specific_view(request,cat_name):
    category = get_object_or_404(Type, title=cat_name)
    products = Product.objects.filter(prod_type=category)
    # paginator = Paginator(products,10)
    return render(request,'productlisting.html',{'prods':products})

def all_view(request):
    products = Product.objects.all()
    return render(request,'productlisting.html',{'prods':products})