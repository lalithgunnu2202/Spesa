from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_view(request):
    return render(request,'create.html')

# @login_required
def generate(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        user = request.user
        Prompt.objects.create(user=user,prompt=prompt)
        messages.info(request,"prompt submitted")
        return redirect('index')
    else:
        return render(request,'create.html')