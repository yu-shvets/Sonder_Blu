# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
