from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    url(r'^(?P<id>\w+)/$', views.game, name='game'),
    url(r'^(play)/(?P<id>\w+)/$', views.play_game, name='play_game'),
    url(r'^(?P<id>\w+)/added/$', views.added_to_cart, name='player_added_to_cart')
]
