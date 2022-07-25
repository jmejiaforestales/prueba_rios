# Generated by Django 1.11.23 on 2019-08-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0027_monitoredresource_resource_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='metriclabel',
            name='user',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(choices=[('OWS:TMS','TMS'), ('OWS:WMS-C','WMS-C'), ('OWS:WMTS','WMTS'), ('OWS:WCS','WCS'), ('OWS:WFS','WFS'), ('OWS:WMS','WMS'), ('OWS:WPS','WPS'), ('other','Not OWS'), ('OWS:ALL','Any OWS'), ('all','All'), ('create','Create'), ('upload','Upload'), ('change','Change'), ('change_metadata','Change Metadata'), ('view_metadata','View Metadata'), ('view','View'), ('download','Download'), ('publish','Publish'), ('remove','Remove'), ('geoserver','Geoserver event')], max_length=16, unique=True),
        ),
    ]
