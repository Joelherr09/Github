# Generated by Django 4.1.3 on 2022-12-20 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipos', '0002_remove_equipo_fundador_equipo_fundador_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='fundador_id',
        ),
        migrations.AddField(
            model_name='equipo',
            name='fundador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='equipos_creados', to=settings.AUTH_USER_MODEL),
        ),
    ]
