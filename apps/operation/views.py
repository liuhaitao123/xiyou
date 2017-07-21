# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse
import json
import os
from xiyou.settings import BASE_DIR

from information.models import HelpCenter
from operation.models import UserMajor

# Create your views here.


class UploadView(View):
	def get(self, request):
		if not request.user.is_authenticated():
			return HttpResponseRedirect(reverse('user:login'))
			
		return render(request, 'upload.html')
		
	def post(self, request):
		#多文件获取
		upload_files = request.FILES.getlist('myfiles')
		
		for file in upload_files:
			if file:
				if not os.path.exists(BASE_DIR+ '/uploads/' + request.user.username):
					os.makedirs(BASE_DIR+ '/uploads/' + request.user.username)
				destination = open(os.path.join(BASE_DIR+ '/uploads/' + request.user.username + '/', file.name),'wb+')
				for chunk in file.chunks():
					destination.write(chunk)
				destination.close()
				
					
		return HttpResponse("上传成功")
		
			
class AboutView(View):
	def get(self, request):
		all_articles = HelpCenter.objects.all()
		return render(request, 'about.html', {'all_articles': all_articles})
		

class CartView(View):
	def get(self, request):
		return render(request, 'cart.html')
		

class ApplyDeleteView(View):
	def post(self, request):
		apply_id = request.POST.get('apply_id', '')
		apply_info = UserMajor.objects.get(pk=int(apply_id))
		apply_info.delete()
		json_data = {'status': 'success', 'msg': '删除成功'}
		return HttpResponse(json.dumps(json_data), content_type="application/json")
		
		
