# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_movie_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='file_location',
            field=models.FileField(max_length=300, null=True, upload_to='movies'),
        ),
    ]
