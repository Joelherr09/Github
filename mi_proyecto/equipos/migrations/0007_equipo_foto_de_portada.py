# Generated by Django 4.1.3 on 2022-12-29 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0006_alter_equipo_fundador'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='foto_de_portada',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
