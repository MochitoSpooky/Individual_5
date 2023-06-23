from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UsuarioForm
from django import forms


def base(request):
    return render(request, 'principal/base.html')
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'principal/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            usuario = form.cleaned_data['usuario']  # Obtener el nombre de usuario
            contraseña = form.cleaned_data['contraseña']
            
            
            # Crea un nuevo usuario
            user = User.objects.create_user(username=usuario, first_name=nombre, last_name=apellido, email=email)
            user.set_password(contraseña)
            user.save()
            
            # Redirecciona a la página de inicio
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    
    return render(request, 'principal/crear_usuario.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')  # Redirecciona a la página 'perfil'
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    return render(request, 'principal/login.html')
def logout_view(request):
    logout(request)
    return redirect('principal/base.html')# Redirecciona a la página principal después del cierre de sesión

from django.shortcuts import render

def profile_view(request):
    user = request.user  # Usuario autenticado
    return render(request, 'principal/perfil.html', {'user': user})
