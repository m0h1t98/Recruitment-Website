# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 06:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clutch', '0008_clutchrecdata_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clutchrecdata',
            name='score',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
