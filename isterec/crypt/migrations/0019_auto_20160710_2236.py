# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypt', '0018_auto_20160708_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptrecdata',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
