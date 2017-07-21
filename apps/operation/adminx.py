# -*- coding:utf-8 -*-
import xadmin
from .models import UserMajor, UserAsk, HighApply, UserCart


class UserMajorAdmin(object):
    list_display = ('id', 'user', 'university', 'major', 'add_time')
    list_display_links = ('user', 'major')
    search_fields = ('user', 'university', 'major')
    list_filter = ('user__username', 'university', 'major', 'add_time')


class UserAskAdmin(object):
    list_display = ('id', 'user', 'problem', 'teacher', 'answer', 'status', 'add_time')
    list_display_links = ('user', 'problem',)
    search_fields = ('user', 'problem', 'teacher')
    list_filter = ('user__username', 'problem', 'teacher', 'add_time')


class HignApplyAdmin(object):
    list_display = ('id', 'user', 'country','real_name', 'type', 'major', 'add_time')
    list_display_links = ('user', 'country')
    search_fields = ('user', 'country', 'type', 'major')
    list_filter = ('user__username', 'country', 'type', 'major', 'add_time')


class UserCartAdmin(object):
    list_display = ('id', 'user', 'store_id', 'store_type', 'nums', 'add_time')
    list_display_links = ('id',)
    search_fields = ('user', 'store_id', 'store_type')
    list_filter = ('user__username', 'store_id', 'store_type', 'add_time')

xadmin.site.register(UserMajor, UserMajorAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(HighApply, HignApplyAdmin)
xadmin.site.register(UserCart, UserCartAdmin)