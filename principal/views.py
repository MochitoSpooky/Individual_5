from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User

def base(request):
    return render(request, 'principal/base.html')
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'principal/lista_usuarios.html', {'usuarios': usuarios})
