# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 14:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypt', '0016_auto_20160708_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptrecdata',
            name='rollno',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid Roll number.', regex='^(\\d{2}|\\d{8})?([a-z]{2}|[A-Z]{2})\\d{2,3}([a-z]{1}|[A-Z]{1})?(\\d{2})?$')]),
        ),
    ]