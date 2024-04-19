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
]