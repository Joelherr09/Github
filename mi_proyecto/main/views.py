from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'main/home.html', {})