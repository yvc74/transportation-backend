# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 22:23
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIimports', '0013_auto_20170215_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('dateRange', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('data', models.TextField(default=None)),
                ('sourceRef', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='APIimports.ApiElement')),
            ],
        ),
    ]
