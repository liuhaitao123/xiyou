# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-20 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_usercart_nums'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='status',
            field=models.IntegerField(choices=[(1, '\u5df2\u4ed8\u6b3e'), (0, '\u672a\u4ed8\u6b3e')], default=0, verbose_name='\u8ba2\u5355\u72b6\u6001'),
        ),
    ]
