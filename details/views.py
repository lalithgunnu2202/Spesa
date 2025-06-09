from django.shortcuts import render, get_object_or_404
from home.models import  *

# Create your views here.
def view_product(request,item_id):
    item = get_object_or_404(Product, id=item_id)
    size = item.size
    products = Product.objects.all()[:4]
    return render(request,'productdetails.html',{'item':item,'products':products,'size':size})