# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

from university.models import Country

# Create your models here.


class WinCase(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=30, default='')
    image = models.ImageField(upload_to=u'wincase/%y/%m', verbose_name=u'照片', max_length=120, default='wincase/default.png')
    country = models.ForeignKey(Country, verbose_name=u'申请国家', null=True)
    education_now = models.CharField(choices=(('college', u'本科'),('graduate', u'研究生'),('mba', u'MBA')), max_length=10, verbose_name=u'学历', default='college')
    education_apply = models.CharField(choices=(('college', u'本科'),('graduate', u'研究生'),('mba', u'MBA')), max_length=10, verbose_name=u'学历', default='graduate')
    university  = models.CharField(verbose_name=u'申请学校', max_length=80, null=True)
    academy = models.CharField(verbose_name=u'毕业院校', max_length=80, null=True)
    major_now = models.CharField(verbose_name=u'当前专业', max_length=40, null=True)
    major_apply = models.CharField(verbose_name=u'申请专业', max_length=40, null=True)
    show_index = models.IntegerField(choices=((1, u'首页展示'),(0, u'首页不展示')), verbose_name=u'是否首页展示', default=0)
    GPA = models.IntegerField(verbose_name=u'平均分', default=0, null= True)
    time = models.DateTimeField(verbose_name=u'offer日期', null=True, blank=True)
    content = models.TextField(verbose_name=u'评价', null=True)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)
	
    class Meta:
        verbose_name = u'成功案例'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=300)
    content = models.TextField(verbose_name=u'内容', null=True, blank=True)
    status = models.IntegerField(verbose_name=u'状态', choices=((0, u'草稿'), (1, u'发布')), default=0)
    country = models.ForeignKey(Country, verbose_name=u'相关国家')
    category = models.CharField(choices=(('gl', u'留学攻略'),('lt', u'留学论坛'),('zx', u'留学咨询')), verbose_name=u'分类', max_length=6, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
