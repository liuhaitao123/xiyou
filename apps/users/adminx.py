# -*- coding:utf-8 -*-
import xadmin
from xadmin import views
from .models import UserProfile, EmailVerifyRecord, BannerIndex, BannerOther


# xadmin后台基础设置
class BaseSettings(object):
    # xadmin开启主体支持
    enable_themes = True
    use_bootswatch = True


# xadmin后台全局设置
class GlobalSettings(object):
    site_title = u'西柚留学网'
    site_footer = u'北京西柚科技有限公司'
    # 左侧菜单项折叠设置
    menu_style = 'accordion'


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
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)