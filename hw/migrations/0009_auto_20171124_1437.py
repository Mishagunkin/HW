# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 14:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0008_auto_20171124_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 24, 14, 37, 26, 379957, tzinfo=utc), verbose_name='Дата аренды'),
        ),
    ]
