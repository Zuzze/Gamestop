from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from .models import Developer
from gamedata.models import Game
from .forms import AddGameForm, ModifyGameForm

@login_required
def index(request):
    try:
        dev_ = Developer.objects.get(user=request.user)
    except Developer.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "Not registered as a developer")
        return HttpResponseRedirect("/error/")

    context = {
        'games' : dev_.games.all(),
        'user' : request.user,
        'user_type': '1',
    }
    return render (request, 'developer/index.html', context)

@login_required
def add_game(request):
    try:
        dev_ = Developer.objects.get(user=request.user)
    except Developer.DoesNotExist:
        messages.add_message(request, messages.INFO,
        "Not registered as a developer")
        return HttpResponseRedirect("/error/")

    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            game_title_ = form.cleaned_data['game_title']
            game_url_ = form.cleaned_data['game_url']
            game_des_ = form.cleaned_data['game_description']
            game_icon_ = form.cleaned_data['game_icon']
            game_price_ = form.cleaned_data['game_price']
            game_category_ = form.cleaned_data['game_category']
            dev_.add_game(game_title_, game_url_, game_price_, game_des_,
                          game_icon_, game_category_)
            return HttpResponseRedirect('/dev/')
    else:
        form = AddGameForm()

    context = {
        'name' : request.user,
        'form' : form,
        'user_type': '1',
    }

    return render (request, 'developer/add_game.html', context)

@login_required
def modify_game(request, game_id):
    try:
        game = Game.objects.get(id=game_id);
    except Game.DoesNotExist:
        messages.add_message(request, messages.INFO, "Game does not exist");
        return HttpResponseRedirect("/error/");

    try:
        dev_ = Developer.objects.get(user=request.user);
    except Developer.DoesNotExist:
        messages.add_message(request, messages.INFO, "Please login as a developer");
        return HttpResponseRedirect("/error/");

    found = False;
    for g in dev_.games.all():
        if g.id == game.id:
            found = True;
    if not found:
        messages.add_message(request, messages.INFO, "You are not the developer of the game. You cannot modify!")
        return HttpResponseRedirect("/error/");

    if request.method == 'POST':
        form = ModifyGameForm(request.POST);
        if form.is_valid():
            print("Form is valid")
            game_title_ = form.cleaned_data['game_title']
            game_url_ = form.cleaned_data['game_url']
            game_des_ = form.cleaned_data['game_description']
            game_icon_ = form.cleaned_data['game_icon']
            game_price_ = form.cleaned_data['game_price']
            game_category_ = form.cleaned_data['game_category']
            dev_.modify_game(game, game_title_, game_url_, game_des_, game_icon_, game_price_, game_category_);
            return HttpResponseRedirect('/dev/')
        else:
            print("Form not valid")
    else:
        form = ModifyGameForm(initial={'game_title': game.title,
                        'game_url': game.url, 'game_description': game.description,
                        'game_icon': game.icon, 'game_price': game.price,
                        'game_category': game.category});

    context = {
        'game' : game,
        'form' : form,
        'user_type': '1',
    }

    return render(request, 'developer/modify_game.html', context);

@login_required
def delete_game(request, game_id):
    try:
        game = Game.objects.get(id=game_id);
    except Game.DoesNotExist:
        messages.add_message(request, messages.INFO, "Game does not exist");
        return HttpResponseRedirect("/error/");

    try:
        dev_ = Developer.objects.get(user=request.user);
    except Developer.DoesNotExist:
        messages.add_message(request, messages.INFO, "Please login as a developer");
        return HttpResponseRedirect("/error/");

    found = False;
    for g in dev_.games.all():
        if g.id == game.id:
            found = True;
    if not found:
        messages.add_message(request, messages.INFO, "You are not the developer of the game. You cannot remove from GameStop");
        return HttpResponseRedirect("/error/");

    game.delete();
    return HttpResponseRedirect("/dev/");
