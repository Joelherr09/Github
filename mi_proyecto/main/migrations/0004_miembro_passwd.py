# Generated by Django 4.1.2 on 2022-11-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='passwd',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]