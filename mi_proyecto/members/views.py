from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import RegisterUserForm, EditProfileForm, BioPerfil
from .models import Perfil
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView



# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            messages.success(request, ("Datos incorrectos, intenta de nuevo"))
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Te has desconectado. Vuelve pronto!"))
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Te has registrado exitosamente!"))
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form':form,
    })

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name= 'authenticate/change-password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'authenticate/password_success.html', {})

class PerfilView(DetailView):
    model = Perfil
    template_name = 'authenticate/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Perfil.objects.all()
        context = super(PerfilView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Perfil, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class EditarPerfilView(UpdateView):
    model = Perfil
    template_name = 'authenticate/profile_bio.html'
    form = BioPerfil
    fields = ['bio', 'ciudad','foto_perfil', 'foto_de_portada']
    success_url = reverse_lazy('index')

class CrearPerfilView(CreateView):
    #form_class = BioPerfil
    model = Perfil
    fields = ['bio', 'ciudad','foto_perfil', 'foto_de_portada']
    template_name = 'authenticate/crear_perfil.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
