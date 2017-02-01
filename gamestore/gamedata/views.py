from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Game
#testing

def games(request):
    context = {
        'all_games' : Game.objects.all()
    }
    return render(request, 'games/games.html', context)

def game(request, gametitle):
    try:
        game = Game.objects.get(title=gametitle)
    except Game.DoesNotExist:
        return HttpResponseRedirect("/games")
    else:
        context = {
            'game' : game,
        }
        return render(request, 'games/game.html', context)
    return HttpResponseRedirect("/games")

def play_game(request, gametitle):
    try:
        game = Game.objects.get(title=gametitle)
    except Game.DoesNotExist:
        return HttpResponseRedirect("/home/")
    else:
        context = {
            'game' : game,
        }
        return render(request, 'games/play.html', context)
    return HttpResponseRedirect("/games")
