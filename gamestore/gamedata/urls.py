from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.games, name='games'),
    url(r'^(?P<gametitle>\w+)/$', views.game, name='game'),
]
