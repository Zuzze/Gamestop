from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    url(r'^game/$', views.game, name='game'),
]
