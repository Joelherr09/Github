from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Equipo
from members.models import Perfil

class CrearEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('equipo_nickname','nombre','foto_perfil', 'foto_de_portada' ,'bio','ciudad',)

        jugadores = forms.ModelMultipleChoiceField(queryset=Perfil.objects.all())
        widgets = {
            'equipo_nickname' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'foto_perfil' : forms.FileInput(attrs={'class':'form-control'}),
            'foto_de_portada' : forms.FileInput(attrs={'class':'form-control'}),
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control'}),
        }
    
class EditarEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('equipo_nickname','nombre','foto_perfil', 'foto_de_portada' ,'bio','ciudad',)

        jugadores = forms.ModelMultipleChoiceField(queryset=Perfil.objects.all())
        widgets = {
            'equipo_nickname' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'foto_perfil' : forms.FileInput(attrs={'class':'form-control'}),
            'foto_de_portada' : forms.FileInput(attrs={'class':'form-control'}),
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control'}),
        }