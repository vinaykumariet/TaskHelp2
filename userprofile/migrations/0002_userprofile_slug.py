# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-09-21 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]