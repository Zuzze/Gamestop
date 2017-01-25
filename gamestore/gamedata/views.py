from django.shortcuts import render
from django.http import HttpResponse
#testing

def games(request):
    return render(request, 'games/games.html', {})
