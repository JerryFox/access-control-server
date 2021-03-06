# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesscodes', '0003_auto_20160705_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codes',
            name='card_number',
            field=models.CharField(blank=True, default=None, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='codes',
            name='keyb_number',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='codes',
            name='valid_from',
            field=models.DateTimeField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='codes',
            name='valid_to',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='valid to'),
        ),
    ]
