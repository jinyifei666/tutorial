# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0020_auto_20170208_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='locationUrl',
            field=models.CharField(blank=True, max_length=200, verbose_name='位置链接'),
        ),
    ]
