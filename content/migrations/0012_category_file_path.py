# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20170529_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='file_path',
            field=models.FilePathField(blank=True, null=True, path='/home'),
        ),
    ]
