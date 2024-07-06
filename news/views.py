from django.shortcuts import render
from django.views.generic import ListView
from .models import News_post

# Create your views here.
class HomePageView(ListView):
  model = News_post
  template_name = 'home.html'