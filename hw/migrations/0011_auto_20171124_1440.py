# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0010_auto_20171124_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата аренды'),
        ),
    ]
