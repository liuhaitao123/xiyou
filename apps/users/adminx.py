# -*- coding:utf-8 -*-
import xadmin
from .models import UserProfile, EmailVerifyRecord, BannerIndex, BannerOther


class UserProfileAdmin(object):
    list_display = ('id', 'nick_name', 'gender', 'mobile', 'username', 'email')
    list_display_links = ('nick_name', 'username', 'email')
    search_fields = ('nick_name', 'username', 'email')
    list_filter = ('nick_name', 'email', 'username', 'gender', 'mobile', 'add_time')


class EmailVerifyRecordAdmin(object):
    list_display = ('code', 'email', 'type', 'send_time')
    list_display_links = ('code', 'email')
    search_fields = ('email',)
    list_filter = ('email', 'send_time')


class BannerIndexAdmin(object):
    list_display = ('title', 'index', 'url', 'add_time')
    list_display_links = ('title',)
    search_fields = ('title', 'index')
    list_filter = ('title', 'index', 'add_time')


class BannerOtherAdmin(object):
    list_display = ('title', 'index', 'url', 'add_time')
    list_display_links = ('title',)
    search_fields = ('title', 'index',)
    list_filter = ('title', 'index', 'add_time')

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(BannerIndex, BannerIndexAdmin)
xadmin.site.register(BannerOther, BannerOtherAdmin)