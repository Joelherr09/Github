# Generated by Django 4.1.3 on 2022-12-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='fundador',
        ),
        migrations.AddField(
            model_name='equipo',
            name='fundador_id',
            field=models.IntegerField(default='1'),
        ),
    ]
