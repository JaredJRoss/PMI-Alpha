# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 14:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clockin', '0015_auto_20170530_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2017, 5, 30), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_in',
            field=models.TimeField(blank=True, default=datetime.time(14, 14, 15, 496996), verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_out',
            field=models.TimeField(blank=True, default=datetime.time(14, 14, 15, 497042), verbose_name='Time Out'),
        ),
    ]
