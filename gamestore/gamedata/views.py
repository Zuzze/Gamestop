from django.shortcuts import render
from django.http import HttpResponse

from .models import Game
#testing

def games(request):
    context = {
        'all_games' : Game.objects.all()
    }
    return render(request, 'games/games.html', context)

def game(request, gametitle):
    context = {
        'game' : Game.objects.get(id=game.id)
    }
    return render(request, 'games/game.html', context)
