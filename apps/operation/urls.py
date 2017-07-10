# -*- coding: utf-8 -*-
from django.conf.urls import url
from operation.views import UploadView, AboutView

urlpatterns = [
	url(r'^upload/$', UploadView.as_view(), name='upload'),
	url(r'^about/$', AboutView.as_view(), name='about'),
]