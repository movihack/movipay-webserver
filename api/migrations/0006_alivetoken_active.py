# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-10 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alivetoken_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='alivetoken',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
