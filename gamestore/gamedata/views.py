from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Game
from player.models import Player, PlayerGameData

def games(request):
    game_cat = ('Action', 'Role Playing', 'FPS', 'Simulation', 'Stratergy', 'Other')
    top_scores = []
    for game in Game.objects.all():
        data = {};
        for game_player in game.players.all():
            game_data = game_player.game_data.get(game=game)
            data['player_name'] = game_player.user.first_name;
            data['score'] = game_data.player_high_score;
            data['game_title'] = game.title;
            data['game_category'] = game.category;
            top_scores.append(data)

    context = {
        'scoreboard' : top_scores,
        'game_categories': game_cat,
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
        try:
            player_game = player_.games.get(title=game.title)
        except Game.DoesNotExist:
            context = {
                'game' : game,
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
