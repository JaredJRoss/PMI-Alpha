# Generated by Django 2.0.2 on 2018-03-01 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('assigned', 'Assigned'), ('in process', 'In Process'), ('converted', 'Converted'), ('recycled', 'Recycled'), ('dead', 'Dead')], max_length=255, null=True, verbose_name='Status of Organization')),
                ('source', models.CharField(blank=True, choices=[('call', 'Call'), ('email', 'Email'), ('existing customer', 'Existing Customer'), ('partner', 'Partner'), ('public relations', 'Public Relations'), ('compaign', 'Campaign'), ('other', 'Other')], max_length=255, null=True, verbose_name='Source of Organization')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_address', to='common.Address')),
                ('assigned_to', models.ManyToManyField(related_name='organization_assigned_to', to='common.CRMUser')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_created_by', to='common.CRMUser')),
                ('teams', models.ManyToManyField(to='common.Team')),
            ],
        ),
    ]