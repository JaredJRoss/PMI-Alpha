# Generated by Django 2.0.2 on 2018-03-01 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
        ('common', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='assigned_to',
            field=models.ManyToManyField(related_name='case_assigned_users', to='common.CRMUser'),
        ),
        migrations.AddField(
            model_name='case',
            name='contacts',
            field=models.ManyToManyField(to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='case',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_created_by', to='common.CRMUser'),
        ),
        migrations.AddField(
            model_name='case',
            name='teams',
            field=models.ManyToManyField(to='common.Team'),
        ),
    ]