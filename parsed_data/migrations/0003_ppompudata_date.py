# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0002_ppompudata_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppompudata',
            name='date',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]