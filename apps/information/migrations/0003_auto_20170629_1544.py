# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-29 07:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0010_university_show_index'),
        ('information', '0002_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wincase',
            options={'verbose_name': '\u6210\u529f\u6848\u4f8b', 'verbose_name_plural': '\u6210\u529f\u6848\u4f8b'},
        ),
        migrations.AddField(
            model_name='wincase',
            name='GPA',
            field=models.IntegerField(default=0, null=True, verbose_name='\u5e73\u5747\u5206'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='academy',
            field=models.CharField(max_length=80, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='content',
            field=models.TextField(null=True, verbose_name='\u8bc4\u4ef7'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Country', verbose_name='\u7533\u8bf7\u56fd\u5bb6'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='education_apply',
            field=models.CharField(choices=[(b'college', '\u672c\u79d1'), (b'graduate', '\u7814\u7a76\u751f'), (b'mba', 'MBA')], default=b'graduate', max_length=10, verbose_name='\u5b66\u5386'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='education_now',
            field=models.CharField(choices=[(b'college', '\u672c\u79d1'), (b'graduate', '\u7814\u7a76\u751f'), (b'mba', 'MBA')], default=b'college', max_length=10, verbose_name='\u5b66\u5386'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='image',
            field=models.ImageField(default=b'wincase/default.png', max_length=120, upload_to='wincase/%y/%m', verbose_name='\u7167\u7247'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='major_apply',
            field=models.CharField(max_length=40, null=True, verbose_name='\u7533\u8bf7\u4e13\u4e1a'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='major_now',
            field=models.CharField(max_length=40, null=True, verbose_name='\u5f53\u524d\u4e13\u4e1a'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='name',
            field=models.CharField(default=b'', max_length=30, verbose_name='\u59d3\u540d'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='offer\u65e5\u671f'),
        ),
        migrations.AddField(
            model_name='wincase',
            name='university',
            field=models.CharField(max_length=80, null=True, verbose_name='\u7533\u8bf7\u5b66\u6821'),
        ),
    ]
