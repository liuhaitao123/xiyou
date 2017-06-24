# -*- coding:utf-8 -*-

import xadmin
from .models import WriteType, Writer, Visa


class WriteTypeAdmin(object):
    list_display = ('name', 'desc', 'add_time')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'add_time')


class WriteAdmin(object):
    list_display = ('name', 'type', 'price', 'add_time')
    list_display_links = ('name',)
    search_fields = ('name', 'type', 'price')
    list_filter = ('name', 'type', 'price', 'add_time')


class VisaAdmin(object):
    list_display = ('name', 'type', 'price', 'desc', 'add_time')
    list_display_links = ('name',)
    search_fields = ('name', 'price', 'type')
    list_filter = ('name', 'type', 'price', 'add_time')

xadmin.site.register(WriteType, WriteTypeAdmin)
xadmin.site.register(Writer, WriteAdmin)
xadmin.site.register(Visa, VisaAdmin)