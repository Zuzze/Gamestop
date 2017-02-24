from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Game
from player.models import Player

def games(request):
    print(Game.objects.filter(category='A'))
    print(Game.objects.filter(category='RP'))
    print(Game.objects.filter(category='FPS'))
    print(Game.objects.filter(category='SM'))
    print(Game.objects.filter(category='SR'))
    print(Game.objects.filter(category='O'))
    context = {
        'games_action' : Game.objects.filter(category='A'),
        'games_rp' : Game.objects.filter(category='RP'),
        'games_fps' : Game.objects.filter(category='FPS'),
        'games_sim' : Game.objects.filter(category='SM'),
        'games_strat' : Game.objects.filter(category='SR'),
        'games_misc' : Game.objects.filter(category='O'),
    }
    return render(request, 'games/games.html', context)

def game(request, id):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return HttpResponseRedirect("/games")
    else:
        context = {
            'game' : game,
        }
        return render(request, 'games/game.html', context)
    return HttpResponseRedirect("/games")

@login_required
def play_game(request, id):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "You have to register as a player")
        return HttpResponseRedirect("/error/")
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return HttpResponseRedirect("/home/")
    else:
        context = {
            'game' : game,
        }
        return render(request, 'games/play.html', context)
    return HttpResponseRedirect("/games")

#@login_required
#def pay(request, gametitle):

@login_required
def added_to_cart(request, id):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "You have to register as a player")
        return HttpResponseRedirect("/error/")
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return HttpResponseRedirect("/home/")
    else:
        context = {
            'game' : game,
        }
        player_.cart_games.add(game)
        return render(request, 'games/added.html', context)
    return HttpResponseRedirect("/games")

@login_required
def removed_from_cart(request, id):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "You have to register as a player")
        return HttpResponseRedirect("/error/")
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return HttpResponseRedirect("/home/")
    else:
        context = {
            'game' : game,
        }
        player_.cart_games.remove(game)
        return render(request, 'games/removed.html', context)
    return HttpResponseRedirect("/games")
