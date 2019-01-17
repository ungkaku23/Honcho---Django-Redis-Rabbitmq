# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 16:43
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0004_auto_20171116_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
