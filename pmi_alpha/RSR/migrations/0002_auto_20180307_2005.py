# Generated by Django 2.0.3 on 2018-03-08 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='Name',
            field=models.CharField(default='None', max_length=60, verbose_name='Skills'),
        ),
    ]
