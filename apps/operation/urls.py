# -*- coding: utf-8 -*-
from django.conf.urls import url
from operation.views import UploadView, AboutView, CartView, ApplyDeleteView

urlpatterns = [
	url(r'^upload/$', UploadView.as_view(), name='upload'),
	url(r'^about/$', AboutView.as_view(), name='about'),
	url(r'^cart/$', CartView.as_view(), name='cart'),
	url(r'^apply_delete/$', ApplyDeleteView.as_view(), name='delete'),
]