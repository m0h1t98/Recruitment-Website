# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 09:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronicle', '0007_auto_20160815_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='chroniclerecdata',
            name='day_to_slot',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
