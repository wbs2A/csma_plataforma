# Generated by Django 2.2.6 on 2019-10-23 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='denuncia',
            old_name='coordenadasX',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='denuncia',
            old_name='coordenadasY',
            new_name='longitude',
        ),
    ]
