# Generated by Django 4.0.4 on 2022-06-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNQV', '0009_plataformas_linkplataforma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataformas',
            name='linkPlataforma',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Link Plataforma'),
        ),
    ]
