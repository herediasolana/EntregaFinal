# Generated by Django 4.0.4 on 2022-06-26 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNQV', '0012_alter_plataformas_imagen_plataformas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataformas',
            name='imagen_plataformas',
            field=models.ImageField(blank=True, null=True, upload_to='plataformas', verbose_name='Imagen Plataformas'),
        ),
    ]
