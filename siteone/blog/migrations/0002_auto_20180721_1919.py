# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-21 19:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 19, 19, 30, 619790, tzinfo=utc)),
        ),
    ]
