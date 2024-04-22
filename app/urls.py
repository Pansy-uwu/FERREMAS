from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),  
    path('nosotros/', views.nosotros, name='nosotros'),  
    path('producto1/', views.producto1, name='producto1'), 
    path('producto2/', views.producto2, name='producto2'), 
    path('producto3/', views.producto3, name='producto3'), 
    path('productos/', views.productos, name='productos'), 
    path('register/', views.register, name='register'),
    path('vistas/admin/', views.admin, name='admin'),
    path('bodeguero/', views.bodeguero, name='bodeguero'), 
    path('cliente/', views.cliente, name='cliente'),
    path('contador/', views.contador, name='contador'), 
    path('vendedor/', views.vendedor, name='vendedor'),  
    path('get_dolar_price/', views.get_dolar_price, name='get_dolar_price'),
]