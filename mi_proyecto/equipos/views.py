from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from .models import Equipo  # importamos el modelo Equipo
from .forms import CrearEquipo, EditarEquipo  # importamos el formulario CrearEquipo
from django.contrib.auth.models import User  # importamos el modelo User
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from members.models import Perfil

# Importamos las vistas basadas en clases y las funciones necesarias

# Creamos las vistas para nuestras aplicaciones


class CrearEquipoPerfilView(CreateView):
    """Vista para crear un nuevo equipo"""
    model = Equipo  # especificamos el modelo que se va a utilizar
    form_class = CrearEquipo  # especificamos el formulario que se va a utilizar
    #fields = '__all__'  # podemos especificar los campos que queremos que aparezcan en el formulario
    template_name = 'equipos/crear-equipo.html'  # nombre de la plantilla que se va a utilizar
    success_url = reverse_lazy('ver-equipos')

    def form_valid(self, form):
        equipo = form.save(commit=False)
        # Obtener el perfil del usuario autenticado
        perfil = self.request.user.perfil
        # Asignar el perfil como fundador del equipo
        equipo.fundador = perfil
        # Guardar el objeto Equipo y obtener su ID
        equipo.save()
        return redirect(self.success_url)

class EditarEquipoPerfilView(UpdateView):
    model = Equipo
    template_name = 'equipos/editar-equipo-perfil.html'
    form_class = EditarEquipo
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_object_or_404(Equipo, pk=self.kwargs['pk'])

@receiver(post_save, sender=Equipo)
def agregar_equipo_al_perfil(sender, instance, created, **kwargs):
    if created:
        perfil = Perfil.objects.get(user=instance.fundador.user)
        perfil.equipos.add(instance)


@receiver(post_save, sender=Equipo)
def add_fundador_as_jugador(sender, instance, created, **kwargs):
    if created:
        instance.jugadores.add(instance.fundador)
        instance.save()


class EquipoPerfilView(DeleteView):
    """Vista para mostrar el perfil de un equipo individual"""
    model = Equipo  # especificamos el modelo que se va a utilizar
    template_name = 'equipos/equipo-perfil.html'  # nombre de la plantilla que se va a utilizar

    def get_context_data(self, *args, **kwargs):
        """Sobrescribimos este método para obtener el equipo actual y añadirlo al contexto de la plantilla"""
        equipos = Equipo.objects.all()  # obtenemos todos los equipos
        context = super(EquipoPerfilView, self).get_context_data(*args, **kwargs)
        page_team = get_object_or_404(Equipo, id=self.kwargs['pk'])  # obtenemos el equipo actual a partir de su id
        context["page_team"] = page_team  # añadimos el equipo al contexto de la plantilla
        return context

def nuevo_perfil_equipo(request):
    return render(request, 'equipos/nuevo-equipo-perfil.html')

def lista_equipos(request):
    equipos = Equipo.objects.all()
    usuarios = User.objects.all()
    context = {'equipos': equipos, 'usuarios': usuarios}
    return render(request, 'equipos/ranking.html', context)

@login_required
def ver_equipos(request):
    usuario = request.user
    perfil = usuario.perfil
    equipos = perfil.equipos.all()
    return render(request, 'equipos/ver_equipos.html', {'equipos': equipos})