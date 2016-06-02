from django.shortcuts import render
from veloblog.models import Post 
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Post

def index(request):
    return HttpResponse("Rango says hey there world!")
