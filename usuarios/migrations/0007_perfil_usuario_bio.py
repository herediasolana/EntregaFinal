# Generated by Django 4.0.4 on 2022-06-25 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_perfil_usuario_imagen_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil_usuario',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
