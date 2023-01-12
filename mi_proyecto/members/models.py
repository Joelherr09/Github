from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from equipos.models import Equipo

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    ciudad = models.CharField(max_length=50)
    equipos = models.ManyToManyField(Equipo, related_name='usuarios')
    foto_perfil = models.ImageField(null=True, blank=True, upload_to="images/")
    foto_de_portada = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('perfil-view', args=[str(self.id)])