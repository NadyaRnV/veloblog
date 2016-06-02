# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from veloblog import views

urlpatterns = patterns('',      
		url(r'^$', views.PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/ 
                                          			     # будет выводиться список постов
		url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/ 
                                        		      # будет выводиться пост с определенным номером
        )	