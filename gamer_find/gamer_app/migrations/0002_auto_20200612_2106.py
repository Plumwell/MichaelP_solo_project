# Generated by Django 2.2 on 2020-06-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=models.ImageField(upload_to='covers'),
        ),
    ]
