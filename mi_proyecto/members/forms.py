from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class EditProfileForm(UserChangeForm):
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class BioPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('bio','ciudad','foto_perfil', 'foto_de_portada')
        
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control'}),
            'foto_perfil' : forms.FileInput(attrs={'class':'form-control'}),
            'foto_de_portada' : forms.FileInput(attrs={'class':'form-control'}),
        }

