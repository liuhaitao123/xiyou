# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class DocView(View):
    def get(self, request):
        return render(request, 'doc.html')


class VisaView(View):
    def get(self, request):
        return render(request, 'visa.html')
