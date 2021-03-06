from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Game
from developer.models import Developer
from player.models import Player, PlayerGameData

def games(request):
    user_type = '0'
    if request.user.is_authenticated():
        try:
            player_ = Player.objects.get(user=request.user)
        except Player.DoesNotExist:
            pass
        else:
            user_type = '2'
        try:
            dev_ = Developer.objects.get(user=request.user)
        except Developer.DoesNotExist:
            pass
        else:
            user_type = '1'
    game_cat = ('Action', 'Role Playing', 'FPS', 'Simulation', 'Stratergy', 'Other')
    context = {
        'game_categories': game_cat,
        'games_action' : Game.objects.filter(category='A'),
        'games_rp' : Game.objects.filter(category='RP'),
        'games_fps' : Game.objects.filter(category='FPS'),
        'games_sim' : Game.objects.filter(category='SM'),
        'games_strat' : Game.objects.filter(category='SR'),
        'games_misc' : Game.objects.filter(category='O'),
        'games_all' : Game.objects.all(),
        'user_type': user_type,
    }
    return render(request, 'games/games.html', context)

def game(request, id):
    user_type = '0'
    if request.user.is_authenticated():
        try:
            player_ = Player.objects.get(user=request.user)
        except Player.DoesNotExist:
            pass
        else:
            user_type = '2'
        try:
            dev_ = Developer.objects.get(user=request.user)
        except Developer.DoesNotExist:
            pass
        else:
            user_type = '1'
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return HttpResponseRedirect("/games")
    else:
        context = {
            'game' : game,
            'user_type': user_type,
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
        try:
            player_game = player_.games.get(title=game.title)
        except Game.DoesNotExist:
            context = {
                'game' : game,
                'user_type': '2',
            }
            player_.cart_games.add(game)
            return render(request, 'games/added.html', context)
        else:
            messages.add_message(request, messages.INFO,
            "You have already purchased the game")
            return HttpResponseRedirect("/error/")
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
