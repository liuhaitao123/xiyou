# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(verbose_name=u'昵称', max_length=50, default='')
    birthday = models.DateTimeField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), default='female', max_length=7)
    address = models.CharField(verbose_name=u'地址', max_length=200, default='')
    mobile = models.CharField(verbose_name=u'电话', max_length=11, null=True, blank=True)
    image = models.ImageField(verbose_name=u'用户头像', upload_to='user/%y/%m', default='user/default.jpg', max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.nick_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code


class BannerIndex(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    image = models.ImageField(upload_to=u'banner_index/%y/%m', verbose_name=u'轮播图')
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=200, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'首页轮播图'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class BannerOther(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    image = models.ImageField(upload_to=u'banner_other/%y/%m', verbose_name=u'轮播图')
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=200, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'其他轮播图'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

