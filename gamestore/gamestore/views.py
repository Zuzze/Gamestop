from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages import get_messages
from django.shortcuts import render
from developer.models import Developer
from player.models import Player

def error_view(request):
    messages_ = get_messages(request)
    message_ = None
    for message_ in messages_:
        if message_ is not None:
            print(message_)
            break

    context = {
        'message' : message_
    }
    if request.user.is_authenticated():
        try:
            player_ = Player.objects.get(user=request.user)
        except Player.DoesNotExist:
            pass
        else:
            context['user_type'] = '2'
        try:
            dev_ = Developer.objects.get(user=request.user)
        except Developer.DoesNotExist:
            pass
        else:
            context['user_type'] = '1'
    return render(request, 'error.html', context)

def own_game(request):
    return render(request, 'own_game.html')
