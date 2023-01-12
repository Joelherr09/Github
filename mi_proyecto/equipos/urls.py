from django.urls import path
from . import views
from .views import CrearEquipoPerfilView, EquipoPerfilView, EditarEquipoPerfilView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('crear-equipo/', CrearEquipoPerfilView.as_view(), name="crear-equipo"),
    path('editar-equipo/<int:pk>', EditarEquipoPerfilView.as_view(), name='editar-equipo'),
    path('<int:pk>/equipo/', EquipoPerfilView.as_view(), name="perfil-equipo"),
    path('lista-equipos/', views.lista_equipos, name='lista-equipos'),
    path('mis-equipos/', views.ver_equipos, name='ver-equipos'),
    path('playground/', views.nuevo_perfil_equipo, name="nuevo-perfil-equipo"),
]