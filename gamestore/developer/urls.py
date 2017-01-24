from django.conf.urls import url
from . import views

urlpatterns = [
    # Developer home page
    url(r'^(?P<username>[\w.@+-]+)$', views.index, name='dev'),
    url(r'^(?P<username>[\w.@+-]+)/(home)$', views.index, name='dev_home'),
    url(r'^(?P<username>[\w.@+-]+)/(add)$', views.add_game, name='dev_add_game'),
]
