# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-12-05 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
