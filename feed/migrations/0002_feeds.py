# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 13:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('posts', models.ManyToManyField(blank=True, related_name='posts', to='feed.Posts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
                'verbose_name': 'Feed',
                'verbose_name_plural': 'Feeds',
            },
        ),
    ]
