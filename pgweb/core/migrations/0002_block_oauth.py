# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-10 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='block_oauth',
            field=models.BooleanField(default=False, help_text='Disallow login to this account using OAuth providers like Google or Microsoft.', verbose_name='Block OAuth login'),
        ),
    ]
