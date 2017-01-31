from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from developer.models import Developer
from player.models import Player

def index(request):
    if request.user.is_authenticated():
        if Developer.objects.get(name=request.user):
            return HttpResponseRedirect('/dev/')
        elif Player.objects.get(name=request.user):
            return HttpResponseRedirect('/player/')
    return render(request, 'homepage/index.html')

def login(request):
    return render(request, 'static/login.html', {})

def register(request):
    return render(request, 'static/register.html', {})
