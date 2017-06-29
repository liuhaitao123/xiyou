# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse

from forms import RegisterForm, LoginForm
from operation.models import HighApply
from users.models import BannerIndex
from information.models import WinCase

# Create your views here.


class RegisterView(View):
	def get(self, request):
		register_form = RegisterForm()
		return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
	def get(self, request):
		return render(request, 'login.html')

	def post(self, request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render(request, 'index.html')
			else:
				return render(request, 'login.html', {'msg':u'用户名或密码错误！'})
		else:
			return render(request, 'login.html', {'login_form':login_form})


class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('user:index'))


class IndexView(View):
	def get(self, request):
		banner_list = BannerIndex.objects.all().order_by('index')[:3]
		win_case_one = WinCase.objects.filter(show_index=1)[:8]
		win_case_two = WinCase.objects.filter(show_index=1)[8:15]
		
		return render(request, 'index.html', {'banner_list': banner_list, 'win_case_one': win_case_one, 'win_case_two': win_case_two})
		
		
class HighApplyView(View):
	def get(self, request):
		return render(request, 'highapply.html')
		
	def post(self, request):
		if not request.user.is_authenticated():
			return HttpResponseRedirect(reverse('user:login'))
		else:
			user_id = request.user.id
			realname = request.POST.get('realname', '')
			country = request.POST.get('country', '')
			type = request.POST.get('type', '')
			major = request.POST.get('major', '')
			high_apply = HighApply()
			high_apply.user_id = user_id
			high_apply.real_name = realname
			high_apply.type = type
			high_apply.country = country
			high_apply.major = major
			high_apply.save()
			return HttpResponseRedirect(reverse('user:highapply'))
			