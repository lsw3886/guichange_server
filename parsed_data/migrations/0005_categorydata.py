# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0004_auto_20170814_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('img', models.IntegerField()),
            ],
        ),
    ]