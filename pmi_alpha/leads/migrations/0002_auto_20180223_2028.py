# Generated by Django 2.0.2 on 2018-02-24 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='assigned_to',
            field=models.ManyToManyField(related_name='lead_assigned_users', to='common.CRMUser'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_created_by', to='common.CRMUser'),
        ),
    ]