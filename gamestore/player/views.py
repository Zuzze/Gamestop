from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Player
from gamedata.models import Game

@login_required
def playerprofile(request):
    try:
        player_ = Player.objects.get(name=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "Not registered as a player")
        return HttpResponseRedirect("/error/")
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

@login_required
def player_buy_game(request, gametitle):
    try:
        player_ = Player.objects.get(name=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO, "Not registered as a player")
        return HttpResponseRedirect("/error/")
    else:
        player_.player_add_game(gametitle)
    return HttpResponseRedirect("/player/")

@login_required
def player_add_to_cart(request, gametitle):
    try:
        player_ = Player.objects.get(name=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO, "Not registered as a player")
        return HttpResponseRedirect("/error/")
    else:
        player_.player_add_to_cart(gametitle)
    return HttpResponseRedirect("/games/")
