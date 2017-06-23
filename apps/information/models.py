# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

from university.models import Country

# Create your models here.


class WinCase(models.Model):

    class Meta:
        verbose_name = u''
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return


class Article(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=300)
    content = models.TextField(verbose_name=u'内容', null=True, blank=True)
    status = models.IntegerField(verbose_name=u'状态', choices=((0, u'草稿'), (1, u'发布')), default=0)
    country = models.ForeignKey(Country, verbose_name=u'相关国家')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
