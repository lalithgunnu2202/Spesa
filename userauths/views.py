from django.shortcuts import render , redirect
from django.contrib.auth import  login , authenticate ,logout
from django.contrib.auth.models import  User
from django.contrib import messages

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        # print(f"USERNAME DEBUG: {username=}")


        if password1!=password2:
            messages.error(request,"Both password do not match")
            return render(request, "signup.html")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"This Username already exits.. Try logging in.")
            return render(request, "signup.html")
        
        user = User.objects.create_user(username=username,password=password1, email=email)
        login(request,user)
        return redirect('index')
    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,"User doesnot exist. Please Register")
            return render(request,'login.html')
    return render(request,'login.html')

def reset_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('password')
        # otp = request.POST.get('otp')
        # tally otp
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request,"Password Changed Succesfully")
            return redirect('login')
        else:
            messages.error(request,"Your Username does not match with out database")
            return render(request,'reset.html')
    else:
        return render(request,'reset.html')
    
def logout_view(request):
    logout(request)
    messages.info(request,"Logged Out successfully")
    return redirect('index')