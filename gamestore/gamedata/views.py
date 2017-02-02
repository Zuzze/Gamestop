from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Game
from player.models import Player

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

@login_required
def play_game(request, gametitle):
    try:
        player_ = Player.objects.get(name=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "You have to register as a player")
        return HttpResponseRedirect("/error/")
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
