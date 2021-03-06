# Generated by Django 2.2 on 2020-06-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='fav',
            field=models.ManyToManyField(related_name='stores', to='board_app.User'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('players', models.IntegerField(max_length=2)),
                ('gametype', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=250)),
                ('fav', models.ManyToManyField(related_name='games', to='board_app.User')),
            ],
        ),
    ]
