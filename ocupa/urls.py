# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('ocupa.views',
	url(r'^$', 'index', name='home'),
    url(r'^questions/$', 'questions', name='questions'),
<<<<<<< HEAD
=======
    url(r'^list/$', 'list', name='list'),
>>>>>>> 61b52e97ba020199e3f8bdea5faafc44491a0ee4
)