# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIimports', '0015_polygon'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='projectName',
            field=models.CharField(default='', max_length=2083),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='point',
            name='projectName',
            field=models.CharField(default='temp', max_length=2083),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='polygon',
            name='projectName',
            field=models.CharField(default='temp', max_length=2083),
            preserve_default=False,
        ),
    ]