from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import *

# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = 'index.html'