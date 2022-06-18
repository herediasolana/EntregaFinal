from django import forms
from usuarios.models import Perfil_usuario


class Perfil_usuario(forms.ModelForm):
    class Meta:
        model = Perfil_usuario
        fields="__all__"