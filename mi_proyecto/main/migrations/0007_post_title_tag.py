# Generated by Django 4.1.2 on 2022-11-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='VoleiChamp', max_length=255),
        ),
    ]