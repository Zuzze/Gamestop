from django.conf.urls import url
from . import views

urlpatterns = [
    # Developer home page
    url(r'^$', views.index, name='dev'),
    url(r'^home/$', views.index, name='dev_home'),
    url(r'^add/$', views.add_game, name='dev_add_game'),
    url(r'^modify/(?P<game_id>[0-9]+)/$', views.modify_game, name='dev_modify_game'),
    url(r'^delete/(?P<game_id>[0-9]+)/$', views.delete_game, name='dev_delete_game'),
]
