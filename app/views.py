from django.shortcuts import render
import requests
from .api import Mindicador
from django.http import JsonResponse


def get_dolar_price(request):
    mindicador = Mindicador('dolar', 2024)
    dolar_price = mindicador.get_dolar_price()
    return JsonResponse({'dolar_price': dolar_price})


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

def admin(request):
    context={}
    return render(request, 'vistas/admin/admin.html', context)

def bodeguero(request):
    context={}
    return render(request, 'vistas/bodeguero/bodeguero.html', context)

def cliente(request):
    context={}
    return render(request, 'vistas/cliente/cliente.html')

def contador(request):
    context={}
    return render(request, 'vistas/contador/contador.html', context)

def vendedor(request):
    context={}
    return render(request, 'vistas/vendedor/vendedor.html', context)