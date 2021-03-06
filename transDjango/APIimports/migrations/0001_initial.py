# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 03:10
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API_element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField()),
                ('query_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.CharField(max_length=2083)),
                ('api_name', models.CharField(max_length=2083)),
                ('source_name', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('orig_daterange', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('canonical_daterange', django.contrib.postgres.fields.ranges.DateRangeField()),
                ('orig_status', models.CharField(max_length=2083)),
                ('canonical_status', models.CharField(max_length=2083)),
                ('source_name', models.CharField(max_length=2083)),
                ('data', models.TextField(default=None)),
                ('source_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIimports.API_element')),
            ],
        ),
    ]
