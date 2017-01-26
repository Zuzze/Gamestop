from django.shortcuts import render
from django.http import HttpResponse
#testing

def index(request):
    context = {
        'user' : request.user
    }
    if request.user.is_authenticated():
        context['username'] = request.user
    return render(request, 'homepage/index.html', context)

def login(request):
    return render(request, 'static/login.html', {})

def register(request):
    return render(request, 'static/register.html', {})
