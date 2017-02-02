from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.playerprofile, name='playerprofile'),
    url(r'^shop/$', views.player_shop_view, name='player_shop_view'),
    url(r'^(?P<gametitle>\w+)/$', views.player_buy_game, name='player_buy_game_view'),
]
