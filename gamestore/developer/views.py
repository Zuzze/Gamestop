from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from .models import Developer
from gamedata.models import Game
from .forms import AddGameForm

@login_required
def index(request):
    try:
        dev_ = Developer.objects.get(name=request.user)
    except Exception as e:
        print(e)
        return HttpResponse("Bad page")

    context = {
        'games' : dev_.games.all(),
        'name' : request.user,
    }
    return render (request, 'developer/index.html', context)

@login_required
def add_game(request):
    try:
        dev_ = Developer.objects.get(name=request.user)
    except Exception as e:
        print(e)
        return HttpResponse("Bad page")

    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            game_title_ = form.cleaned_data['game_title']
            game_url_ = form.cleaned_data['game_url']
            new_game_ = Game(title=game_title_, url=game_url_, dev=dev_)
            new_game_.save()
            return HttpResponseRedirect('/dev/')
    else:
        form = AddGameForm()

    context = {
        'name' : request.user,
        'form' : form,
    }

    return render (request, 'developer/add_game.html', context)
