from django.conf.urls import url
from . import views

urlpatterns = [
    # Developer home page
    url(r'^$', views.index, name='dev'),
    url(r'^home/$', views.index, name='dev_home'),
    url(r'^add/$', views.add_game, name='dev_add_game'),
]
