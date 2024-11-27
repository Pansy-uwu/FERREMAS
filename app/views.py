from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import csrf_exempt
from .api import Mindicador
from django.http import JsonResponse
import json
import os
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
from .apisimple import get_data
from django.contrib.auth import authenticate, login
from django.contrib import messages


def mostrar_datos(request):
    datos = get_data('')  # Reemplaza 'endpoint' con el endpoint real que quieras usar
    return render(request, 'mostrar_datos.html', {'datos': datos})

def get_dolar_price(request):
    mindicador = Mindicador('dolar', 2024)
    dolar_price = mindicador.get_dolar_price()
    return JsonResponse({'dolar_price': dolar_price})
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def nosotros(request):
    context = {}
    return render(request, 'nosotros.html', context)

def producto1(request):
    context = {}
    return render(request, 'producto1.html', context)

def producto2(request):
    context = {}
    return render(request, 'producto2.html', context)

def producto3(request):
    context = {}
    return render(request, 'producto3.html', context)

def productos(request):
    context = {}
    return render(request, 'productos.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)

def admin(request):
    context = {}
    return render(request, 'vistas/admin/admin.html', context)

def bodeguero(request):
    context = {}
    return render(request, 'vistas/bodeguero/bodeguero.html', context)

def cliente(request):
    context = {}
    return render(request, 'vistas/cliente/cliente.html')

def contador(request):
    context = {}
    return render(request, 'vistas/contador/contador.html', context)

def vendedor(request):
    context = {}
    return render(request, 'vistas/vendedor/vendedor.html', context)

# Configuración de Webpay
commerce_code = "597055555532"
api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"

def init_transaction(request):
    return_url = request.build_absolute_uri('/app/webpay/commit/')
    tx = Transaction(WebpayOptions(commerce_code, api_key, IntegrationType.TEST))
    response = tx.create(buy_order='ordenCompra12345678', session_id='sesion1234557545', amount=1000, return_url=return_url)
    return redirect(response['url'] + '?token_ws=' + response['token'])

@csrf_exempt
def init_transaction_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        amount = float(data['monto'])
        return_url = request.build_absolute_uri('/app/webpay/commit/')
        tx = Transaction(WebpayOptions(commerce_code, api_key, IntegrationType.TEST))
        response = tx.create(buy_order='ordenCompra12345678', session_id='sesion1234557545', amount=amount, return_url=return_url)
        return JsonResponse({'url': response['url'] + '?token_ws=' + response['token']})

def commit_transaction(request):
    token = request.GET.get("token_ws")
    tx = Transaction(WebpayOptions(commerce_code, api_key, IntegrationType.TEST))
    response = tx.commit(token)

    if response['status'] == 'AUTHORIZED':
        context = {
            'response': {
                'buy_order': response['buy_order'],
                'amount': response['amount'],
                'transaction_date': response['transaction_date'],
                'status': response['status']
            }
        }
        return render(request, 'success.html', context)
    else:
        return render(request, 'failure.html', {'response': response})
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal después de iniciar sesión correctamente
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')
