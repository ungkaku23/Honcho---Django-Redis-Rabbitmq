# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 14:25
from __future__ import unicode_literals

import django.db.models.deletion
import enumfields.fields
from django.conf import settings
from django.db import migrations, models

import campaigns.providers.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('django_mailbox', '0005_auto_20160523_2240'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoolMailbox',
            fields=[
                ('mailbox_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True,
                                      serialize=False, to='django_mailbox.Mailbox')),
                ('status_description', models.TextField(blank=True, editable=False)),
                ('status', enumfields.fields.EnumField(enum=campaigns.providers.models.ConnectionStatus, max_length=32)),
            ],
            bases=('django_mailbox.mailbox',),
        ),
        migrations.CreateModel(
            name='EmailAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail address')),
                ('sender_name', models.TextField(blank=True)),
                ('signature', models.TextField(blank=True)),
                ('default', models.BooleanField(default=False)),
                ('incoming', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='providers.CoolMailbox')),
            ],
        ),
        migrations.CreateModel(
            name='SmtpConnectionSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, default=None,
                                         help_text='Example: smtp+ssl://myusername:mypassword@someserver <br /><br />Be sure to urlencode your username and password should they contain illegal characters (like @, :, etc).',
                                         null=True, verbose_name='URI')),
                ('status', enumfields.fields.EnumField(default='UNKNOWN', editable=False, enum=campaigns.providers.models.ConnectionStatus,
                                                       max_length=32)),
                ('status_description', models.TextField(blank=True, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='emailaccount',
            name='outgoing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='providers.SmtpConnectionSettings'),
        ),
        migrations.AddField(
            model_name='emailaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_accounts',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='emailaccount',
            unique_together=set([('user', 'email')]),
        ),
        migrations.AddField(
            model_name='coolmailbox',
            name='last_uid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coolmailbox',
            name='status',
            field=enumfields.fields.EnumField(default='UNKNOWN', editable=False, enum=campaigns.providers.models.ConnectionStatus,
                                              max_length=32),
        ),
    ]
