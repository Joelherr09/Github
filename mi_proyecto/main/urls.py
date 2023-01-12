from django.urls import path, include
#from .views import HomeView
from . import views

urlpatterns = [
    #path('', HomeView.as_view(), name="home"),
    #path('home/', HomeView.as_view(), name="home"),
    path('', views.index, name="index"),
    path('home/', views.index, name="index"),
]