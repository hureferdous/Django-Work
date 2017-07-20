from django.conf.urls import url
from . import views

urlpatterns = [
    #/cloth/
    url(r'^$', views.index, name='index'),
    url(r'^$', views.say_hello, name='say_hello'),


]
