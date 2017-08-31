from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^processMoney$', views.giveGold),
    url(r'^reset$', views.reset),
]
