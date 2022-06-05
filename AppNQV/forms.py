from django import forms

CATEGORIAS=(
    ('accion', 'ACCION'),
    ('drama','DRAMA'),
    ('suspenso','SUSPENSO'),
    ('terror','TERROR'),
    ('documental','DOCUMENTAL'),
    ('romatica','ROMANTICA'),
)

class PeliculasFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    duracion= forms.TimeField()
    clasificacion= forms.ChoiceField(choices=CATEGORIAS)
    fechaDeEstreno= forms.DateField()
    oscar= forms.BooleanField()
    ratingIMDB= forms.FloatField()
    linkTrailer= forms.URLField()