from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Player, PlayerGameData
from gamedata.models import Game

@login_required
def playerprofile(request):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "Not registered as a player")
        return HttpResponseRedirect("/error/")
    context = {
        'gameData' : PlayerGameData.objects.filter(player=player_),
        #'gameData':
        'user': request.user,
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
def player_cart(request):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO, "Not registered as a player")
        return HttpResponseRedirect("/error/")
    else:
        context = {
            'cart_games': player_.cart_games,
        }
        return render(request, 'player/cart.html', context)


@login_required
def player_update_game_data(request):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO, "Not registered as a player")
        return HttpResponseRedirect("/error/")
    else:
        try:
            game_ = Game.objects.get(id=request.POST['gameId'])
        except Game.DoesNotExist:
            messages.add_message(request, messages.INFO, "Player not registered "
            "to play this game. Something very wrong!")
            return HttpResponseRedirect("/error/")
        else:
            try:
                game_data = PlayerGameData.objects.get(player=player_, game=game_)
            except PlayerGameData.DoesNotExist:
                messages.add_message(request, messages.INFO, "Player not registered "
                "to play this game. Something very wrong!")
                return HttpResponseRedirect("/error/")
            else:
                game_data.update_game_data(request.POST)
    return HttpResponse("")


""" Skipping payment and adds all the games in the cart. For testing. Remove
    later """
@login_required
def player_buy_game_test(request):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO, "Not registered as a player")
        return HttpResponseRedirect("/error/")
    else:
        player_.player_add_game()
    return HttpResponseRedirect("/home/")
