# Generated by Django 2.2 on 2020-06-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgame_app', '0005_remove_game_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.FileField(default='none', upload_to='covers'),
            preserve_default=False,
        ),
    ]
