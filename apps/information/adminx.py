# -*- coding:utf-8 -*-
import xadmin
from .models import WinCase, Article


class ArticleAdmin(object):
    list_display = ('id', 'title', 'content', 'status', 'country', 'add_time')
    list_display_links = ('title',)
    search_fields = ('title', 'status', 'country')
    list_filter = ('title', 'status', 'country', 'add_time')

xadmin.site.register(Article, ArticleAdmin)
