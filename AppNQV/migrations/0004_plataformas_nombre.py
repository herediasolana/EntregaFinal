# Generated by Django 4.0.4 on 2022-06-05 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNQV', '0003_alter_peliculas_ratingimdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataformas',
            name='nombre',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
