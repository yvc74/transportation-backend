# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 03:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIimports', '0012_auto_20170215_0334'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CIPline',
        ),
        migrations.DeleteModel(
            name='CIPpoint',
        ),
        migrations.DeleteModel(
            name='StPJline',
        ),
        migrations.AlterField(
            model_name='point',
            name='dateRange',
            field=django.contrib.postgres.fields.ranges.DateRangeField(),
        ),
    ]