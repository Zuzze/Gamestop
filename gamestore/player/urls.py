from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.playerprofile, name='playerprofile'),
    url(r'^shop/$', views.player_shop_view, name='player_shop_view'),
    url(r'^cart/$', views.player_cart, name='player_cart'),
    url(r'^update_game_data/$', views.player_update_game_data, name='player_update_game_data_view'),

    #payment
    url(r'^payment/success$', views.payment_success, name='payment_success_view'),
    url(r'^payment/cancel$', views.payment_cancel, name='payment_cancel_view'),
    url(r'^payment/error$', views.payment_error, name='payment_error_view'),
]
