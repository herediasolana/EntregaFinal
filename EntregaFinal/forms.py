from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from usuarios.models import Perfil_usuario


class User_registration_form(UserCreationForm):
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita su Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password1', 'password2', 'email']
        help_texts = {k:''for k in fields}# por cada valor en fields ponele vacío, es decir, no quiero que los campos tengan texto de ayuda

class User_edit_form(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff','password1', 'password2']
        help_texts = {k:''for k in fields}# por cada valor en fields ponele vacío, es decir, no quiero que los campos tengan texto de ayuda