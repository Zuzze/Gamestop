from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth

#from django.core.context_processors import csrf

from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Logged in!")
    else:
        form = LoginForm()

    context = { 'form': form }
    return render(request, 'accounts/login.html', context)

def logout(request):
    return HttpResponse("Logged out!")
