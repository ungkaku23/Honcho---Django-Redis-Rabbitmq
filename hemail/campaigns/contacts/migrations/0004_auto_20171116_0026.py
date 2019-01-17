# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 00:26
from __future__ import unicode_literals

from django.db import migrations

import common.fields


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0003_auto_20170906_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timezone',
            field=common.fields.TimeZoneField(blank=True, max_length=32),
        ),
    ]
