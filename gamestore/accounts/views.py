from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .forms import LoginForm, RegistrationForm
from developer.models import Developer
from player.models import Player

from hashlib import md5

SALT = "gamestop-coolapp";

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username_ = form.cleaned_data['username']
        password_ = form.cleaned_data['password']
        if form.login_allowed:
            user = User.objects.get(username=username_)
            try:
                dev_ = Developer.objects.get(user=user)
            except Developer.DoesNotExist:
                try:
                    player_ = Player.objects.get(user=user)
                except Player.DoesNotExist:
                    pass
                else:
                    if player_.registered == False:
                        messages.add_message(request, messages.INFO,
                            "Kindly activate your account");
                    return HttpResponseRedirect("/error/")
            else:
                if dev_.registered == False:
                    messages.add_message(request, messages.INFO,
                        "Kindly activate your account");
                return HttpResponseRedirect("/error/")

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
        email_ = form.cleaned_data['email']
        password_ = form.cleaned_data['password']
        re_password_ = form.cleaned_data['re_password']
        user_type_ = form.cleaned_data['user_type']
        user = User.objects.create_user(first_name=name_, username=username_, password=password_, email=email_)

        activation_string = user.email + SALT;
        activation_key = md5(activation_string.encode("ascii")).hexdigest();

        print("Activation Url - " + settings.BASE_URL + "/activate?user=" + str(user.id) + "&activation_key=" + activation_key)

        if (user_type_ == '1'):
            dev_ = Developer(user=user)
            dev_.registered = False;
            dev_.activation_key = activation_key;
            dev_.save();
        else:
            player_ = Player(user=user)
            player_.registered = False;
            player_.activation_key = activation_key;
            player_.save()
        #login(request, user)
        return HttpResponseRedirect("/home")

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def acitvate_account_view(request):
    if request.GET.get('user') is None or request.GET.get('activation_key') is None:
        messages.add_message(request, messages.INFO, "Activation link is not valid");
        return HttpResponseRedirect("/error/")

    try:
        user = User.objects.get(id=request.GET['user'])
    except User.DoesNotExist:
        messages.add_message(request, messages.INFO, "Activation link is not valid");
        return HttpResponseRedirect("/error/")

    #Compute hash again
    #activation_string = user.email + SALT;
    #activation_key = md5(activation_string.encode("ascii")).hexdigest();

    #if (activation_key != request.GET['activation_key']):
    #    messages.add_message(request, messages.INFO, "Activation link is not valid");
    #    return HttpResponseRedirect("/error/")

    try:
        dev_ = Developer.objects.get(user=user)
    except Developer.DoesNotExist:
        try:
            player_ = Player.objects.get(user=user)
        except Player.DoesNotExist:
            messages.add_message(request, messages.INFO, "Not register as player or developer");
            return HttpResponseRedirect("/error/")
        else:
            if player_.activation_key != request.GET['activation_key']:
                messages.add_message(request, messages.INFO, "Activation link is not valid");
                return HttpResponseRedirect("/error/")
            player_.registered = True;
    else:
        if dev_.activation_key != request.GET['activation_key']:
            messages.add_message(request, messages.INFO, "Activation link is not valid");
            return HttpResponseRedirect("/error/")
        dev_.registered = True;
    login(request, user)
    return HttpResponseRedirect("/home")
