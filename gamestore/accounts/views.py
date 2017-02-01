from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from .forms import LoginForm, RegistrationForm
from developer.models import Developer
from player.models import Player

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username_ = form.cleaned_data['username']
        #password_ = form.cleaned_data['password']
        user = User.objects.get(username=username_)
        #user = authenticate(username=username_, password=password_)
        #if user is None:
        #    context = { 'form': form,
        #    'message': 'Incorrect username or password. Try again.',
        #    }
        #    return render(request, "accounts/login.html", context)
        login(request, user)
        return HttpResponseRedirect("/home/")

    context = { 'form': form }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/home/")

def register_view(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name_ = form.cleaned_data['name']
        username_ = form.cleaned_data['username']
        password_ = form.cleaned_data['password']
        re_password_ = form.cleaned_data['re_password']
        user_type_ = form.cleaned_data['user_type']
        user = User.objects.create_user(name_, username_, password_)
        if (user_type_ == '1'):
            dev_ = Developer(name=username_)
            dev_.save()
            url = "developer/index.html"
        else:
            player_ = Player(name=username_)
            player_.save()
            url = "player/profile.html"
        login(request, user)
        return HttpResponseRedirect(url)

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
