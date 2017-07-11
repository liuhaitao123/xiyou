# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse
import json

from information.models import HelpCenter

# Create your views here.


class UploadView(View):
	def get(self, request):
		return render(request, 'upload.html')
	
	
class AboutView(View):
	def get(self, request):
		all_articles = HelpCenter.objects.all()
		return render(request, 'about.html', {'all_articles': all_articles})
