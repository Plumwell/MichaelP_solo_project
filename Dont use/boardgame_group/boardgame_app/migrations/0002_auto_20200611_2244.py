# Generated by Django 2.2 on 2020-06-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgame_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lname',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='name', max_length=35),
            preserve_default=False,
        ),
    ]
