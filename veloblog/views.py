# -*- coding: utf-8 -*-
from django.shortcuts import render
from veloblog.models import Post 
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Post

