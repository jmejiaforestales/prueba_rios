# Generated by Django 2.2.24 on 2022-02-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0065_auto_20220217_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='alternate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
