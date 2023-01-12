from django.urls import path

from ..Web import consumers

websocket_urlpatterns = [
    path('ws/notificaciones/', consumers.NotificacionesConsumer),
]
