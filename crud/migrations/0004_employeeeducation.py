# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-28 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20180927_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name', models.CharField(max_length=50)),
                ('edu_uni', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.Employee')),
            ],
            options={
                'db_table': 'emp_education',
            },
        ),
    ]
