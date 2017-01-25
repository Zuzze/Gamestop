from django.shortcuts import render
from django.http import HttpResponse
#testing

def index(request):
    return render(request, 'homepage/index.html', {})

def login(request):
    return render(request, 'static/login.html', {})

def register(request):
    return render(request, 'static/register.html', {})
