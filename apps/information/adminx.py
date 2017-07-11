# -*- coding:utf-8 -*-
import xadmin
from .models import WinCase, Article, HelpCenter


class ArticleAdmin(object):
    list_display = ('id', 'title', 'content', 'status', 'country', 'add_time')
    list_display_links = ('title',)
    search_fields = ('title', 'status', 'country')
    list_filter = ('title', 'status', 'country', 'add_time')
	
	
class WinCaseAdmin(object):
    list_display = ('id', 'name', 'content', 'university', 'academy', 'show_index', 'add_time')
    list_display_links = ('name',)
    search_fields = ('name', 'country', 'university')
    list_filter = ('name', 'university', 'country', 'show_index', 'add_time')


class HelpCenterAdmin(object):
    list_display = ('id', 'title', 'content','status', 'add_time')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title', 'content', 'add_time')

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(WinCase, WinCaseAdmin)
xadmin.site.register(HelpCenter, HelpCenterAdmin)
