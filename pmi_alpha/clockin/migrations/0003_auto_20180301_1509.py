# Generated by Django 2.0.2 on 2018-03-01 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clockin', '0002_auto_20180223_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='time_in',
            field=models.TimeField(blank=True, default=datetime.time(15, 9, 9, 364390), verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_out',
            field=models.TimeField(blank=True, default=datetime.time(15, 9, 9, 364421), verbose_name='Time Out'),
        ),
    ]
