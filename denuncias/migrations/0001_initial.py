# Generated by Django 2.2.6 on 2019-10-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenadasX', models.FloatField()),
                ('coordenadasY', models.FloatField()),
                ('observacao', models.TextField()),
                ('conhece_origem', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('contato', models.CharField(max_length=30)),
            ],
        ),
    ]