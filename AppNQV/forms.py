from datetime import datetime
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

def current_year():
    return datetime.date.today().year
def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]

#class PeliculasFormulario(forms.Form):
#    nombre= forms.CharField(max_length=40)
#    duracion= forms.TimeField()
#    clasificacion= forms.ChoiceField(choices=CATEGORIAS)
#    fechaDeEstreno= forms.DateField()
#    oscar= forms.BooleanField()
#    ratingIMDB= forms.FloatField()
#    linkTrailer= forms.URLField()
class DateInput(forms.DateInput):
    input_type = 'date'


class PeliculasFormulario(forms.ModelForm):
    year: forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model = Peliculas
        fields="__all__"
        widgets = {
            'nombre': forms.TextInput,
            'duracion': forms.NumberInput,
            'fechaDeEstreno':DateInput(),
        }


class PlataformasFormulario(forms.ModelForm):
    class Meta:
        model = Plataformas
        fields="__all__"
        help_texts={'duracion':'duracion estimada en minutos'}
#       fields= ['nombre', 'cantidadUsuarios', 'cantidadPeliculasDisponibles']--> puedo seleccionar los campos que necesite!

class ActoresFormulario(forms.ModelForm):
    class Meta:
        model = Actores
        fields="__all__"
        widgets = {
            'fechaDeNacimiento':DateInput(),
        }
