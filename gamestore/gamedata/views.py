from django.shortcuts import render
from django.http import HttpResponse

from .models import Game
#testing

def games(request):
    context = {
        'all_games' : Game.objects.all()
    }
    return render(request, 'games/games.html', context)

def game(request):
    context = {
        'all_games' : Game.objects.all()
    }
    return render(request, 'games/game.html', context)
