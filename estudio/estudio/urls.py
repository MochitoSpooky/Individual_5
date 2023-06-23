"""
URL configuration for Individual_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from principal.views import base, lista_usuarios, crear_usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', base, name='base'),  # Ruta para la página base.html (página principal)
    path('usuarios/', lista_usuarios, name='lista_usuarios'),  # Ruta para la página lista_usuarios.html
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='principal/base.html'), name='logout'),
]

