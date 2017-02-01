from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Player
from gamedata.models import Game

@login_required
def playerprofile(request):
    try:
        player_ = Player.objects.get(name=request.user)
    except Exception as e:
        print(e)
        return HttpResponse("Bad page")
    context = {
        'games' : player_.games.all(),
        'username': request.user,
        'user_type': '2',
    }
    return render(request, 'player/index.html', context)

@login_required
def player_shop_view(request):
    context = {
        'all_games': Game.objects.all(),
        'username': request.user,
        'user_type': '2',
    }
    return render(request, 'player/shop_games.html', context)
