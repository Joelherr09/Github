from django.urls import path
from . import views
from .views import PerfilView, UserEditView, PasswordsChangeView, EditarPerfilView, CrearPerfilView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    path('<int:pk>/perfil/', PerfilView.as_view(), name="perfil-view"),
    path('edit_profile/', UserEditView.as_view(), name="edit-profile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='authenticate/change-password.html')),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success', views.password_success, name="password_success"),
    path('perfil-editar/<int:pk>', EditarPerfilView.as_view(), name="perfil-editar"),
    path('crear-perfil/', CrearPerfilView.as_view(), name="crear-perfil"),
]