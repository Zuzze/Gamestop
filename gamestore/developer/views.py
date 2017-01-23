from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response

from .models import Developer
from gamedata.models import Game
from .forms import AddGameForm

"""
Developer home page.
"""
def index(request, username):
    print(username)
    dev_ = Developer.objects.get(name=username)
    for game_ in dev_.games.all():
        print(game_.title)
    context = { 'games' : dev_.games.all() }
    return render (request, 'developer/index.html', context)

"""
Developer add game
"""
def add_game(request, username):
    dev_ = Developer.objects.get(name=username)
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            game_title_ = form.cleaned_data['game_title']
            game_url_ = form.cleaned_data['game_url']
            new_game_ = Game(title=game_title_, url=game_url_, dev=dev_)
            new_game_.save()
            return HttpResponseRedirect('home')
    else:
        form = AddGameForm()
    context = {
        'name' : username,
        'form' : form,
    }

    return render (request, 'developer/add_game.html', context)
