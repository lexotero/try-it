# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congress', '0002_auto_20161103_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]