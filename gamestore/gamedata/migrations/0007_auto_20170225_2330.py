# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-25 23:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gamedata', '0006_auto_20170225_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='last_purchased',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 25, 23, 30, 27, 997814, tzinfo=utc)),
        ),
    ]
