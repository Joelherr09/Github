from django.shortcuts import render

# Create your views here.


def notificaciones_index(request):
    return render(request, 'notificaciones/notificaciones.html', {})