# Generated by Django 2.2.5 on 2019-11-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='signup_confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
