from django.shortcuts import render
from django.http import HttpResponse
#testing

def index(request):
    return HttpResponse("Welcome to homepage of game store")
