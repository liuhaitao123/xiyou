# -*- coding:utf-8 -*-
import xadmin
from .models import Country, University, MajorField, Major, Scenery, Level

# Register your models here.


class CountryAdmin(object):
    list_display = ('id', 'name', 'add_time',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

	
class LevelAdmin(object):
    list_display = ('id', 'name', 'add_time',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

	
class UniversityAdmin(object):
    list_display = ('name', 'country', 'type', 'rank',)
    list_display_links = ('name',)
    search_fields = ('name', 'country',)
    list_filter = ('name', 'country', 'type', 'add_time',)


class MajorFieldAdmin(object):
    list_display = ('name', 'desc', 'add_time')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'add_time',)


class MajorAdmin(object):
    list_display = ('name', 'desc', 'type', 'field', 'add_time')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'field', 'type', 'add_time',)


class SceneryAdmin(object):
    list_display = ('title', 'university', 'image', 'image1', 'image2', 'image3', 'image4', 'add_time')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title', 'add_time',)

xadmin.site.register(Country, CountryAdmin)
xadmin.site.register(Level, LevelAdmin)
xadmin.site.register(University, UniversityAdmin)
xadmin.site.register(MajorField, MajorFieldAdmin)
xadmin.site.register(Major, MajorAdmin)
xadmin.site.register(Scenery, SceneryAdmin)