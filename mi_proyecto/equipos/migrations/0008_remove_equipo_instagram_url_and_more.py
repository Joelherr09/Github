# Generated by Django 4.1.3 on 2022-12-29 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0007_equipo_foto_de_portada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='website_url',
        ),
    ]
