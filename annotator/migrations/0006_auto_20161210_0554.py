# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0005_auto_20161210_0543'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='annotation',
            unique_together=set([('key', 'cui')]),
        ),
    ]