# Generated by Django 3.0.8 on 2020-07-06 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200705_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='llave_foranea',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='polls.Proyecto'),
        ),
    ]
