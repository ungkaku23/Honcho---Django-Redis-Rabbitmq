# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 23:55
from __future__ import unicode_literals

import django.db.models.deletion
import enumfields.fields
from django.conf import settings
from django.db import migrations, models

import campaigns.templates.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post_office', '0006_attachment_mimetype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('emailtemplate_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True,
                                      serialize=False, to='post_office.EmailTemplate')),
                ('sharing', enumfields.fields.EnumField(default='PERSONAL', enum=campaigns.templates.models.EmailTemplateSharingStatus,
                                                        help_text='Template sharing level', max_length=32)),
            ],
            bases=('post_office.emailtemplate',),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='templates.Folder'),
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]