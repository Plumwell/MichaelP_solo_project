# Generated by Django 2.2 on 2020-06-11 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0008_remove_merchant_patrons'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='patrons',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, related_name='patrons', to='board_app.User'),
            preserve_default=False,
        ),
    ]
