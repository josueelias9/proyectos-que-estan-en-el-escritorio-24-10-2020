# Generated by Django 3.0.8 on 2020-10-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0035_auto_20200723_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_geojson', models.CharField(default='', max_length=100)),
                ('juego_de_arrays', models.CharField(default='', max_length=100)),
                ('informacion', models.CharField(default='', max_length=100)),
            ],
        ),
    ]