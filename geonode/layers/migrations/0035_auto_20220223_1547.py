# Generated by Django 2.2.24 on 2022-02-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0034_auto_20210329_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='store',
            field=models.CharField(max_length=255, verbose_name='Store'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='storeType',
            field=models.CharField(max_length=255, verbose_name='Storetype'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='typename',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Typename'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='workspace',
            field=models.CharField(max_length=255, verbose_name='Workspace'),
        ),
    ]
