# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('ocupa.views',
	url(r'^$', 'index', name='home'),
    url(r'^questions/$', 'questions', name='questions'),
)