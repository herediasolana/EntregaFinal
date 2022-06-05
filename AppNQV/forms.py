from django import forms

CATEGORIAS=(
    ('accion', 'ACCION'),
    ('drama','DRAMA'),
    ('suspenso','SUSPENSO'),
    ('terror','TERROR'),
    ('documental','DOCUMENTAL'),
    ('romantica','ROMANTICA'),
)

class PeliculasFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    duracion= forms.TimeField()
    clasificacion= forms.ChoiceField(choices=CATEGORIAS)
    fechaDeEstreno= forms.DateField()
    oscar= forms.BooleanField()
    ratingIMDB= forms.FloatField()
    linkTrailer= forms.URLField()

class PlataformasFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    cantidadUsuarios= forms.IntegerField()
    cantidadPeliculasDisponibles= forms.IntegerField()
    precioSuscripcion= forms.DecimalField(max_digits=6, decimal_places=2)

class ActoresFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    edad= forms.IntegerField()
    origen= forms.CharField(max_length=40)
    fechaDeNacimiento= forms.DateField()
