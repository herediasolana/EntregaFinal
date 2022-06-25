from django import forms
from usuarios.models import Perfil_usuario

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class user_profile_form(forms.ModelForm):
    class Meta:
        model = Perfil_usuario
        fields="__all__"

class User_registration_form(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput)
    first_name= forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput)
    last_name= forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput)
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita su Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password1', 'password2']
        help_texts = {k:''for k in fields}# por cada valor en fields ponele vacío, es decir, no quiero que los campos tengan texto de ayuda

class User_edit_form(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff']
        help_texts = {k:''for k in fields}# por cada valor en fields ponele vacío, es decir, no quiero que los campos tengan texto de ayuda