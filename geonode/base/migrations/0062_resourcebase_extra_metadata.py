# Generated by Django 2.2.24 on 2022-01-26 14:04

from django.db import migrations
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0061_auto_20211117_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='extra_metadata',
            field=django_jsonfield_backport.models.JSONField(blank=True, default=list, null=True),
        ),
    ]
