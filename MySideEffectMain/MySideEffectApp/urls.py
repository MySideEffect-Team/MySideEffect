#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-


from django.conf.urls import url

from . import views

app_name = 'MySideEffectApp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
   # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
   # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
   # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
