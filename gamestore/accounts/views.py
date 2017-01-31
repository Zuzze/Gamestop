from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm, RegistrationForm
from developer.models import Developer
from player.models import Player

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_ = form.cleaned_data['username']
            password_ = form.cleaned_data['password']
            user = authenticate(username=username_, password=password_)
            if user is None:
                context = { 'form': form,
                'message': 'Incorrect username or password. Try again.',
                }
                return render(request, "accounts/login.html", context)
            login(request, user)
            if Developer.objects.get(name=user):
                return HttpResponseRedirect("/dev/")
            elif Player.objects.get(name=user):
                return HttpResponseRedirect("/player/")
    else:
        form = LoginForm()

    context = { 'form': form }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/home/")

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name_ = form.cleaned_data['name']
            username_ = form.cleaned_data['username']
            password_ = form.cleaned_data['password']
            user = User.objects.create_user(name_, username_, password_)
            user_type_ = form.cleaned_data['user_type']
            if (user_type_ == '1'):
                dev_ = Developer(name=username_)
                dev_.save()
                url = "developer/index.html"
            else:
                player_ = Player(name=username_)
                player_.save()
                url = "player/profile.html"
            login(request, user)
        return render(request, url)

    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
