# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.


class Country(models.Model):
    name = models.CharField(verbose_name=u'国家名称', max_length=150)
    image = models.ImageField(upload_to=u'university/country/%y/%m', verbose_name=u'logo', max_length=150, null=True)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'国家'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(verbose_name=u'学历层次名称', max_length=50)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)\


    class Meta:
        verbose_name = u'学历层次'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class University(models.Model):
    name = models.CharField(verbose_name=u'学校名称', max_length=200)
    image = models.ImageField(verbose_name=u'首页展示图', upload_to=u'university', max_length=200)
    logo = models.ImageField(verbose_name=u'校徽', upload_to=u'university/logo', max_length=200, default='university/logo/logo.jpg')
    english_name = models.CharField(verbose_name=u'英文名', max_length=200)
    country = models.ForeignKey(Country, verbose_name=u'所属国家')
    city = models.CharField(verbose_name=u'所属城市', max_length=100)
    type = models.CharField(choices=(('private',u'私立'), ('public', u'公立')), default='public', max_length=13, verbose_name=u'学校类型')
    level = models.ForeignKey(Level, verbose_name=u'学历层次', null=True)
    bulid_time = models.DateTimeField(verbose_name=u'建校时间', null=True, blank=True)
    tea_stu = models.CharField(verbose_name=u'师生比', max_length=10)
    students = models.IntegerField(verbose_name=u'学生人数', default=0)
    tuition = models.IntegerField(verbose_name=u'学费', default=0)
    accept_rate = models.CharField(verbose_name=u'录取率', max_length=30)
    address = models.CharField(verbose_name=u'学校地址', max_length=10)
    end_time = models.DateTimeField(verbose_name=u'截止日期', null=True, blank=True)
    url = models.CharField(verbose_name=u'网址', max_length=200)
    rank = models.IntegerField(verbose_name=u'排名', default=0)
    desc = models.TextField(verbose_name=u'简介', null=True, blank=True)
    college_gpa = models.FloatField(verbose_name=u'本科GPA', default=75.00)
    college_toefl = models.FloatField(verbose_name=u'本科托福', default=110.00)
    college_ielts = models.FloatField(verbose_name=u'本科雅思', default=6.00)
    graduate_gpa = models.FloatField(verbose_name=u'研究生GPA', default=75)
    graduate_toefl = models.FloatField(verbose_name=u'研究生托福', default=110.00)
    graduate_ielts = models.FloatField(verbose_name=u'研究生雅思', default=6.00)
    click_num = models.IntegerField(verbose_name=u'点击数', default=0)
    show_index = models.IntegerField(verbose_name=u'是否首页显示', choices=((1, u'首页显示'),(0, u'首页不显示')), default=0)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'大学信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_all_major(self):
        return self.major_set.all()


class MajorField(models.Model):
    name = models.CharField(verbose_name=u'专业方向名称', max_length=40)
    desc = models.CharField(verbose_name=u'描述', null=True, blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'专业方向'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name		


class Major(models.Model):
    name = models.CharField(verbose_name=u'专业名称', max_length=50)
    english_name = models.CharField(verbose_name=u'英文名称', max_length=100, null=True, blank=True)
    university = models.ForeignKey(University, verbose_name=u'所属大学', null=True, blank=True)
    desc = models.CharField(verbose_name=u'专业描述', null=True, blank=True, max_length=100)
    type = models.CharField(choices=(('college', u'本科'), ('graduate', u'研究生')), default='college', max_length=15, verbose_name=u'学位类型')
    field = models.ForeignKey(MajorField, verbose_name=u'专业方向')
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'专业信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Scenery(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=50)
    university = models.ForeignKey(University, verbose_name=u'所属大学')
    image = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    image1 = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    image2 = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    image3 = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    image4 = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    image5 = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    image6 = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    image7 = models.ImageField(upload_to=u'university/scenery/%y/%m', verbose_name=u'校园风光')
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'校园风光'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

