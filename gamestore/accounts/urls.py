
from django.conf.urls import url
from . import views

urlpatterns = [
    # Developer home page
    url(r'^login/$', views.login, name='login_view'),
    url(r'^logout/$', views.logout, name='logout_view'),
]
