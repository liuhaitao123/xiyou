# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
#设置图片显示
from django.views.static import serve
from xiyou.settings import MEDIA_ROOT

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^captche/', include('captcha.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'', include('apps.users.urls', namespace='user')),
    url(r'', include('apps.service.urls', namespace='service')),
    url(r'', include('apps.operation.urls', namespace='operation')),
    url(r'', include('apps.university.urls', namespace='university')),
]
