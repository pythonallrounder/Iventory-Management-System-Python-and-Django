from django.shortcuts import render, redirect
from .models import *
from inventory.form import * 
from django import forms

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def laptop(request):
    items = Laptop.objects.all()
    data = {
        
        'items':items,
        'header' :'Laptop'
    }
    return render(request,'index.html',data)
    
def desktop(request):
    items = Desktop.objects.all()
    
    data = {
        
        'items':items,
        'header' :'Desktop'
    }
    return render(request,'index.html',data)
       
def mobile(request):
    items = Mobile.objects.all()
    data = {
        
        'items':items,
        'header' :'Mobile'
    }
    return render(request,'index.html',data)
 
 
def add_laptop(request):
    if request.method =="POST":
        form=laptopform(request.POST)
         
        if form.is_valid():
            form.save()
            return redirect('index')
         
    else:
        form = laptopform()
        return render(request, 'add_new.html',{'form':form})   

    
def add_desktop(request):
    if request.method =="POST":
        form=desktopform(request.POST)
         
        if form.is_valid():
            form.save()
            return redirect('index')
         
    else:
        form = desktopform()
        return render(request, 'add_new.html',{'form':form}) 


def add_mobile(request):
    if request.method =="POST":
        form=mobileform(request.POST)
         
        if form.is_valid():
            form.save()
            return redirect('index')
         
    else:
        form = mobileform()
        return render(request, 'add_new.html',{'form':form}) 
        