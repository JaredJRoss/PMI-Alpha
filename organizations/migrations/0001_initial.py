# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20170926_1752'),
        ('common', '0002_auto_20170926_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('assigned', 'Assigned'), ('in process', 'In Process'), ('converted', 'Converted'), ('recycled', 'Recycled'), ('dead', 'Dead')], max_length=255, null=True, verbose_name='Status of Organizations')),
                ('source', models.CharField(blank=True, choices=[('call', 'Call'), ('email', 'Email'), ('existing customer', 'Existing Customer'), ('partner', 'Partner'), ('public relations', 'Public Relations'), ('compaign', 'Campaign'), ('other', 'Other')], max_length=255, null=True, verbose_name='Source of Organizations')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Organizations', to='accounts.Account')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizationsaddress', to='common.Address')),
            ],
        ),
    ]