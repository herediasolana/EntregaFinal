# Generated by Django 4.0.4 on 2022-06-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNQV', '0002_actores_apellido_actores_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='ratingIMDB',
            field=models.FloatField(blank=True, null=True),
        ),
    ]