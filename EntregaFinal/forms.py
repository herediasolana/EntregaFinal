from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class User_registration_form(UserCreationForm):
    nombre =forms.CharField()
    apellido =forms.CharField()
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita su Contraseña', widget=forms.PasswordInput)



    class Meta:
        model = User
        fields = ['username','nombre', 'apellido', 'email', 'password1', 'password2']
        help_texts = {k:''for k in fields}# por cada valor en fields ponele vacío, es decir, no quiero que los campos tengan texto de ayuda

class User_edit_form(UserCreationForm):
    nombre =forms.CharField()
    apellido =forms.CharField()
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repita su Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','nombre', 'apellido', 'email', 'password1', 'password2']
        help_texts = {k:''for k in fields}# por cada valor en fields ponele vacío, es decir, no quiero que los campos tengan texto de ayuda