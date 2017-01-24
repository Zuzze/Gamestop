
from django.conf.urls import url
from . import views

urlpatterns = [
    # Developer home page
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^register/$', views.register_view, name='register_view'),
]
