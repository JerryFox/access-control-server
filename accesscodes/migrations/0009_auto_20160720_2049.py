# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-20 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesscodes', '0008_auto_20160719_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='valid_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='valid_to',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_begin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
