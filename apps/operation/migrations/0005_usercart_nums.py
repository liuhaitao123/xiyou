# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-19 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20170703_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='nums',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u6570\u91cf'),
        ),
    ]