# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIimports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressGeocode',
            fields=[
                ('rating', models.IntegerField(primary_key=True, serialize=False)),
                ('lon', models.DecimalField(decimal_places=10, max_digits=13)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=13)),
                ('addy', models.CharField(max_length=2083)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
