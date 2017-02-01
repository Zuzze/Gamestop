from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from developer.models import Developer
from player.models import Player

from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated():
        try:
            player_ = Player.objects.get(name=request.user)
        except Player.DoesNotExist:
            pass
        else:
            return HttpResponseRedirect('/player/')
        try:
            dev_ = Developer.objects.get(name=request.user)
        except Developer.DoesNotExist:
            pass
        else:
            return HttpResponseRedirect('/dev/')
    return render(request, 'homepage/index.html')

def login(request):
    return render(request, 'static/login.html', {})

def register(request):
    return render(request, 'static/register.html', {})
