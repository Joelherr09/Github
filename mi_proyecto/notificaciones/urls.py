from django.urls import path, include
from . import views

urlpatterns = [
    path("notificaciones/", views.notificaciones_index, name="notificaciones-index"),
]