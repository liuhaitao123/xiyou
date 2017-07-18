# -*- coding: utf-8 -*-
from django.conf.urls import url
from operation.views import UploadView, AboutView, CartView

urlpatterns = [
	url(r'^upload/$', UploadView.as_view(), name='upload'),
	url(r'^about/$', AboutView.as_view(), name='about'),
	url(r'^cart/$', CartView.as_view(), name='cart'),
]