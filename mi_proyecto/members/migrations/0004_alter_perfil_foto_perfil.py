# Generated by Django 4.1.3 on 2022-11-14 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_perfil_instagram_url_perfil_twitter_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
