# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-23 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_major_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='type',
            field=models.CharField(choices=[(b'college', '\u672c\u79d1'), (b'graduate', '\u7814\u7a76\u751f')], default=b'college', max_length=15, verbose_name='\u5b66\u4f4d\u7c7b\u578b'),
        ),
    ]