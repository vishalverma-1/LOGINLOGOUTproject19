#-------------CREATE PAGE-----------------
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import appy
from django.contrib.auth.models import auth
def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        obj=appy.objects.create(name=name,mobile=mobile,password=password)
        if password==confirm_password:
            obj.save()
            return redirect('login')
        else:
            return HttpResponse("invalid password")   
    else:
        return render(request,'create.html')    

#-----------LOGIN PAGE-----------------


def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        data=appy.objects.get(name=name,password=password)
        if(data is not None):
            return redirect('home')
    else:
        return render(request,'login.html')
    

#-------------HOME PAGE-------------

def home(request):
    return render(request,'home.html')

#------------LOGOUT PAGE-----------------

def logout(request):
    auth.logout(request)
    return redirect('login')
       