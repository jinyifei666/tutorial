# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0021_location_locationurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='pointInfo',
            field=models.CharField(blank=True, max_length=200, verbose_name='信息点'),
        ),
    ]
