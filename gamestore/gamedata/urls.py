from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    url(r'^(\w{2})/$', views.game, name='game'),
]
