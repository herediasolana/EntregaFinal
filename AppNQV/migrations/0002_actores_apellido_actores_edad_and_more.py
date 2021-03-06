# Generated by Django 4.0.4 on 2022-06-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNQV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actores',
            name='apellido',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='actores',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actores',
            name='fechaDeNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actores',
            name='nombre',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='actores',
            name='origen',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='clasificacion',
            field=models.CharField(choices=[('accion', 'ACCION'), ('drama', 'DRAMA'), ('suspenso', 'SUSPENSO'), ('terror', 'TERROR'), ('documental', 'DOCUMENTAL'), ('romatica', 'ROMANTICA')], default='drama', max_length=20),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='duracion',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='fechaDeEstreno',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='linkTrailer',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='nombre',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='oscar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='ratingIMDB',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plataformas',
            name='cantidadPeliculasDisponibles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plataformas',
            name='cantidadUsuarios',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plataformas',
            name='precioSuscripcion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
