from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Equipo(models.Model):
    fundador = models.ForeignKey('members.Perfil', on_delete=models.CASCADE, related_name='equipos_fundados')
    jugadores = models.ManyToManyField('members.Perfil', related_name='usuarios', blank=True)
    equipo_nickname = models.CharField(max_length=20)
    nombre = models.CharField('Nombre del Equipo',max_length=50)
    bio = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=50)
    foto_perfil = models.ImageField(null=True, blank=True, upload_to="images/")
    foto_de_portada = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('perfil-equipo', args=[str(self.id)])



class Partido(models.Model):
    nombre = models.CharField(max_length=500)
    direccion = models.CharField(max_length=500)
    equipos = models.ManyToManyField(Equipo, blank=True)
    #gimnasio = models.ForeignKey(Gimnasio, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=500)
    fecha_partido = models.DateField("Fecha del Partido")

    def __str__(self):
        return self.nombre