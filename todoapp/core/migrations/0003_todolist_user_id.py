# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180128_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='user_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]