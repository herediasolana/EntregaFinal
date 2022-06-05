from django import forms
from AppNQV.models import Actores, Peliculas, Plataformas

CATEGORIAS=(
    ('accion', 'ACCION'),
    ('drama','DRAMA'),
    ('suspenso','SUSPENSO'),
    ('terror','TERROR'),
    ('documental','DOCUMENTAL'),
    ('romantica','ROMANTICA'),
)

#class PeliculasFormulario(forms.Form):
#    nombre= forms.CharField(max_length=40)
#    duracion= forms.TimeField()
#    clasificacion= forms.ChoiceField(choices=CATEGORIAS)
#    fechaDeEstreno= forms.DateField()
#    oscar= forms.BooleanField()
#    ratingIMDB= forms.FloatField()
#    linkTrailer= forms.URLField()

class PeliculasFormulario(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields="__all__"

class PlataformasFormulario(forms.ModelForm):
    class Meta:
        model = Plataformas
        fields="__all__"
#       fields= ['nombre', 'cantidadUsuarios', 'cantidadPeliculasDisponibles']--> puedo seleccionar los campos que necesite!

class ActoresFormulario(forms.ModelForm):
    class Meta:
        model = Actores
        fields="__all__"
