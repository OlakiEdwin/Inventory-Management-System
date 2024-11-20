from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import RemoteUserBackend

# Create your views here.

def login_page(request):
    if request.method=="POST":
        user=authenticate(request,username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            form=AuthenticationForm()
            errormessage="User or Password is incorret!"
            return render(request, 'login.html', {'form':form, 'error':errormessage})
        else:
            login(request,user)
            return redirect(request, 'home')
    else:
        form=AuthenticationForm()
        return render(request,'login.html', {'form':form})

def signup_page(request):
    return render(request, 'signup.html')

def home_page(request):
    return render(request, 'index.html')