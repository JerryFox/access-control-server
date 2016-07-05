# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 14:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accesscodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codes',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
