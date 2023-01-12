"""
Este código es una lista de patrones de URL que Django utilizará para mapear solicitudes entrantes
a vistas de aplicaciones. Cada patrón de URL consiste en una ruta (una cadena que representa una dirección)
y una vista (una función que maneja la solicitud y devuelve una respuesta).
Algunos comentarios sobre cada línea del código:

path('admin/', admin.site.urls): Este patrón de URL redirige todas las solicitudes que comiencen con "admin/" a las vistas del panel de administración de Django.

path('',include("main.urls")): Este patrón de URL incluye todos los patrones de URL de la aplicación "main". Esto significa que Django buscará patrones adicionales de URL en el archivo "urls.py" de la aplicación "main" para manejar solicitudes que no se hayan manejado por otros patrones de URL.

path('', include("django.contrib.auth.urls")): Este patrón de URL incluye todos los patrones de URL predefinidos de Django para la autenticación y la gestión de usuarios. Esto incluye vistas para iniciar sesión, cerrar sesión, restablecer contraseñas, etc.

path('members/', include('django.contrib.auth.urls')): Este patrón de URL es similar al anterior, pero incluye los patrones de URL de autenticación y gestión de usuarios solo para solicitudes que comiencen con "members/".

path('members/', include('members.urls')): Este patrón de URL incluye todos los patrones de URL de la aplicación "members" para solicitudes que comiencen con "members/".

path('equipos/', include('equipos.urls')): Este patrón de URL incluye todos los patrones de URL de la aplicación "equipos" para solicitudes que comiencen con "equipos/".
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('', include("django.contrib.auth.urls")),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    #path('equipos/', include('django.contrib.auth.urls')),
    path('equipos/', include('equipos.urls')),
    path('notificaciones/', include('notificaciones.urls')),
    path('chat/', include("chat.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
