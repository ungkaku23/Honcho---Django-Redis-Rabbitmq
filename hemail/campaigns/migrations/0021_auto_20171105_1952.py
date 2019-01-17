# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 19:52
from __future__ import unicode_literals

from django.db import migrations

import campaigns.models
import common.fields


class Migration(migrations.Migration):
    dependencies = [
        ('campaigns', '0020_auto_20171025_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='problems',
            field=common.fields.EnumSetField(
                default=[campaigns.models.CampaignProblems('no_steps'), campaigns.models.CampaignProblems('no_contacts')], editable=False,
                enum=campaigns.models.CampaignProblems),
        ),
        migrations.AddField(
            model_name='step',
            name='problems',
            field=common.fields.EnumSetField(default=[campaigns.models.StepProblems('empty_step')], editable=False,
                                             enum=campaigns.models.StepProblems),
        ),
    ]