# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-28 02:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0015_author_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('version', models.IntegerField(default=0)),
                ('upload_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('size', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y%m%d', verbose_name='作者照片'),
        ),
    ]
