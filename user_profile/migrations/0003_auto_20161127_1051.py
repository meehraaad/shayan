# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-27 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_writing_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writing',
            name='author',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Writing',
        ),
    ]
