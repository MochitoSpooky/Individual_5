from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    usuario = forms.CharField(max_length=100)  # Campo adicional para el nombre de usuario
    contraseña = forms.CharField(widget=forms.PasswordInput())

