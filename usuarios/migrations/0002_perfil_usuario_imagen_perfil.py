# Generated by Django 4.0.4 on 2022-06-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil_usuario',
            name='imagen_perfil',
            field=models.ImageField(default='', upload_to='imagen_perfil'),
            preserve_default=False,
        ),
    ]
