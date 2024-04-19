from django.shortcuts import render
from django.contrib import admin

# Create your views here.

def index(request):
    context={}
    return render(request, 'index.html', context)

def login(request):
    context={}
    return render(request, 'login.html', context)

def nosotros(request):
    context={}
    return render(request, 'nosotros.html', context)

def producto1(request):
    context={}
    return render(request, 'producto1.html', context)

def producto2(request):
    context={}
    return render(request, 'producto2.html', context)

def producto3(request):
    context={}
    return render(request, 'producto3.html', context)

def productos(request):
    context={}
    return render(request, 'productos.html', context)

def register(request):
    context={}
    return render(request, 'register.html', context)