# Generated by Django 2.2 on 2020-06-12 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardgame_app', '0004_game_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='poster',
        ),
    ]
