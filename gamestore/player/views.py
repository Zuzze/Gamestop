from django.shortcuts import render
from django.http import HttpResponse
#testing

def playerprofile(request):
    return render(request, 'player/profile.html', {})
