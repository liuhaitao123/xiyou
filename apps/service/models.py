# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.


class WriteType(models.Model):
    name = models.CharField(verbose_name=u'类型名称', max_length=150)
    desc = models.CharField(verbose_name=u'类型描述', max_length=150)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'文书类型'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(verbose_name=u'文书名称', max_length=50)
    english_name = models.CharField(verbose_name=u'英文名', max_length=50)
    image = models.ImageField(upload_to=u'writer', verbose_name=u'封面')
    type = models.ForeignKey(WriteType, verbose_name=u'文书类型')
    desc = models.CharField(verbose_name=u'描述', max_length=300, null=True, blank=True)
    price = models.FloatField(verbose_name=u'价格', default=0)
    detail = models.TextField(verbose_name=u'详情', null=True, blank=True)
    service = models.TextField(verbose_name=u'服务保障', null=True, blank=True)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'文书'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Visa(models.Model):
    name = models.CharField(verbose_name=u'签证名称', max_length=50)
    english_name = models.CharField(verbose_name=u'英文名', max_length=50)
    image = models.ImageField(upload_to=u'visa', verbose_name=u'封面')
    type = models.CharField(choices=(('xs', u'学生签证'), ('ly', u'旅游签证'), ('ye', u'1+2套餐'), ('bg', u'包过套餐')), verbose_name=u'签证类型', max_length=8)
    desc = models.CharField(verbose_name=u'描述', max_length=300, null=True, blank=True)
    price = models.FloatField(verbose_name=u'价格', default=0)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'签证'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


