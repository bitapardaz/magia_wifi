# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_remove_movie_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='link',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
