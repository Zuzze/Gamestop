from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#from django.core.context_processors import csrf

from .forms import LoginForm, RegistrationForm
from developer.models import Developer

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_ = form.cleaned_data['username']
            password_ = form.cleaned_data['password']
            user = authenticate(username=username_, password=password_)
            if user is not None:
                login(request, user)
                return HttpResponse("Logged in!")
            else:
                return HttpResponse("No such user!")
    else:
        form = LoginForm()

    context = { 'form': form }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponse("Logged out!")

def register_view(request):
    #if request.method == 'POST':
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
        return HttpResponse("Account created")

    #else:
    #    form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
