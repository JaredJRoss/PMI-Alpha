# Generated by Django 2.0.2 on 2018-03-01 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clockin', '0003_auto_20180301_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='time_in',
            field=models.TimeField(blank=True, default=datetime.time(15, 56, 49, 688041), verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_out',
            field=models.TimeField(blank=True, default=datetime.time(15, 56, 49, 688070), verbose_name='Time Out'),
        ),
    ]
