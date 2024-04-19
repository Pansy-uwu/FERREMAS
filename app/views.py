from django.shortcuts import render
from django.contrib import admin

# Create your views here.

def index(request):
    context={}
    return render(request, 'index.html', context)
