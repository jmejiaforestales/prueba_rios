# Generated by Django 2.2.24 on 2022-02-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0032_uploadsizelimit'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='store_spatial_files',
            field=models.BooleanField(default=True),
        ),
    ]
