# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-27 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accesscodes', '0010_auto_20160727_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='code_type',
            new_name='code_input',
        ),
        migrations.AlterUniqueTogether(
            name='code',
            unique_together=set([('code_input', 'code_number')]),
        ),
    ]
