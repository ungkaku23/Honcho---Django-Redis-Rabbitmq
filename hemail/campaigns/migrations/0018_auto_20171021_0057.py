# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 00:57
from __future__ import unicode_literals

from django.db import migrations

import common.fields


class Migration(migrations.Migration):
    dependencies = [
        ('campaigns', '0017_step_offset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='timezone',
            field=common.fields.TimeZoneField(blank=True, max_length=32),
        ),
    ]
