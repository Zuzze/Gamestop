from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Player, PlayerGameData
from gamedata.models import Game
from hashlib import md5

secret_key = "1cb99704bf0d36de9d83a740009c37de";
BASE_URL = 'http://localhost:8000';

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
        """ For payment """
        pid = str(player_.id) #+ player_.user.first_name;
        amount  = 0; sid = "gamestop2017";
        for game in player_.cart_games.all():
            amount += game.price

        checksum_str = "pid={}&sid={}&amount={}&token={}".format(pid, sid,
                        amount, secret_key)
        checksum = md5(checksum_str.encode("ascii")).hexdigest();
        context = {
            'cart_games': player_.cart_games,
            'amount': amount,
            'sid': sid,
            'pid': pid,
            'checksum': checksum,
            'success_url': BASE_URL + '/player/payment/success',
            'cancel_url': BASE_URL + '/player/payment/cancel',
            'error_url': BASE_URL + '/player/payment/error',
        }
        return render(request, 'player/cart.html', context)


@login_required
def player_update_game_data(request):
    try:
        player_ = Player.objects.get(user=request.user)
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO, "Not registered as a player")
        return HttpResponseRedirect("/error/")

    if request.method == 'POST':
        gameId = request.POST['gameId']
    elif request.method == 'GET':
        gameId = request.GET['gameId']

    try:
        game_ = Game.objects.get(id=gameId)
    except Game.DoesNotExist:
        messages.add_message(request, messages.INFO, "Player not registered to play this game.")
        return HttpResponseRedirect("/error/")

    try:
        game_data = PlayerGameData.objects.get(player=player_, game=game_)
    except PlayerGameData.DoesNotExist:
        messages.add_message(request, messages.INFO, "Player not registered to play this game. Something very wrong!")
        return HttpResponseRedirect("/error/")

    if request.method == 'POST':
        print("Updating info")
        game_data.update_game_data(request.POST)
    elif request.method == 'GET':
        print("Sending Game save state")
        return HttpResponse(game_data.game_save_data)
    else:
        messages.add_message(request, messages.INFO, "Method not allowed")
        return HttpResponseRedirect("/error/")
    return HttpResponse("")

def validate_payment_response(get_data):
    pid_ = get_data['pid']
    ref_ = get_data['ref']
    result_ = get_data['result']
    checksum_ = get_data['checksum']

    checksum_str = "pid={}&ref={}&result={}&token={}".format(pid_,
                    ref_, result_, secret_key)
    checksum = md5(checksum_str.encode("ascii")).hexdigest();
    if (checksum != checksum_):
        return False, "Checksum does not match"

    return True, ""

def payment_success(request):
    if request.method != 'GET':
        messages.add_message(request, messages.INFO, "Error in payment");
        return HttpResponseRedirect("/error/")

    """ Validate the parameters in GET """
    ret, msg = validate_payment_response(request.GET)
    if (ret == False):
        messages.add_message(request, messages.INFO, msg)
        return HttpResponseRedirect("/error/")
    try:
        player_ = Player.objects.get(id=int(request.GET['pid']))
    except Player.DoesNotExist:
        messages.add_message(request, messages.INFO, "Not registered as a player")
        return HttpResponseRedirect("/error/")
    else:
        player_.player_add_game()
    return HttpResponseRedirect("/home/")

@login_required
def payment_cancel(request):
    messages.add_message(request, messages.INFO, "User has cancelled the payment")
    return HttpResponseRedirect("/error/")

@login_required
def payment_error(request):
    messages.add_message(request, messages.INFO, "There was some error in payment. Please try again")
    return HttpResponseRedirect("/error/")
