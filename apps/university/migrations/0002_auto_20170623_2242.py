# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-23 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='type',
            field=models.CharField(choices=[(b'private', '\u79c1\u7acb'), (b'public', '\u516c\u7acb')], default=b'public', max_length=13, verbose_name='\u5b66\u6821\u7c7b\u578b'),
        ),
    ]
