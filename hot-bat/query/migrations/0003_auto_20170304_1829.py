# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-05 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_auto_20170304_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='battedballdata',
            options={'managed': False, 'verbose_name_plural': 'Batted Ball Data'},
        ),
        migrations.AlterModelOptions(
            name='regulardata',
            options={'managed': False, 'verbose_name_plural': 'Regular Data'},
        ),
    ]