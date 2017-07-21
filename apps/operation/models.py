# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from users.models import UserProfile
from university.models import University, Major

# Create your models here.


class UserMajor(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    university = models.ForeignKey(University, verbose_name=u'学校')
    major = models.ForeignKey(Major, verbose_name=u'专业')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'申请时间')

    class Meta:
        verbose_name = u'申请专业'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.major


class UserAsk(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    problem = models.CharField(max_length=300, verbose_name=u'问题')
    answer = models.CharField(max_length=300, verbose_name=u'回答', null=True, blank=True)
    teacher = models.CharField(verbose_name=u'回答者', max_length=30, null=True, blank=True)
    status = models.IntegerField(choices=((1, u'已解决'),(0, u'未解决')), default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'提问时间')

    class Meta:
        verbose_name = u'用户问题'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.problem


class HighApply(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    real_name = models.CharField(verbose_name=u'姓名', max_length=40, null=True)
    country = models.CharField(verbose_name=u'意向国家', max_length=30)
    type = models.CharField(verbose_name=u'意向层次', max_length=30)
    major = models.CharField(verbose_name=u'意向专业', max_length=30)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'申请时间')

    class Meta:
        verbose_name = u'高端申请'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.country


class UserCart(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    store_id = models.IntegerField(default=0, verbose_name=u'类型id')
    store_type = models.IntegerField(choices=((1, u'文书'), (2, u'签证')), default=1, verbose_name=u'购物车类型')
    nums = models.IntegerField(verbose_name=u'数量', null=True, blank=True)
    status = models.IntegerField(choices=((1, u'已付款'),(0, u'未付款')), default=0, verbose_name=u'订单状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'加入时间')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = verbose_name	

    def __unicode__(self):
        return self.user

