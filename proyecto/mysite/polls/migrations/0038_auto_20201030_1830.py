# Generated by Django 3.0.8 on 2020-10-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0037_auto_20201029_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface_geojson',
            name='tipo_de_geojson',
            field=models.CharField(choices=[('SP', 'Point'), ('MP', 'MultiPoint'), ('SL', 'LineString'), ('ML', 'MultiLineString'), ('SG', 'Polygon'), ('MG', 'MultiPolygon'), ('GC', 'GeometryCollection')], default='CE', max_length=2),
        ),
    ]
