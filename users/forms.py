from django import forms
from .models import  User

class LoginForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = [
                'email',
                'password_hash'
                ]
        labels = {
                'password_hash': 'Contraseña',
                'email': 'Correo Electrónico',
                }

class RegisterForm(forms.ModelForm):
    bio = forms.CharField(label= 'Acerca de ti', required=False, widget=forms.Textarea(attrs={'rows':5, 'cols':23}))
    class Meta:
        model = User
        fields = [
                'username',
                'full_name',
                'email',
                'password_hash',
                'bio'
                ]
        labels = {
                'username': 'Nombre de Usuario',
                'full_name': 'Nombre Completo',
                'email': 'Correo electrónico',
                'password_hash': 'Contraseña',
                'bio': 'Acerca de ti',
                }

