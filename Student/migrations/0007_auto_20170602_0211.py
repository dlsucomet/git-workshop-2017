# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 18:11
from __future__ import unicode_literals

import Student.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_auto_20170602_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='units',
            field=Student.models.MinMaxFloat(),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=Student.models.MinMaxFloat(),
        ),
    ]
