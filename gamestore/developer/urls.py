from django.conf.urls import url
from . import views

urlpatterns = [
    # Developer home page
    url(r'^(?P<username>[\w.@+-]+)$', views.index, name='index'),
    url(r'^(?P<username>[\w.@+-]+)/(home)$', views.index, name='index'),
    url(r'^(?P<username>[\w.@+-]+)/(add)$', views.add_game, name='index'),
]
