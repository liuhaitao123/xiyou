# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from forms import RegisterForm, LoginForm

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
        return render(request, 'index.html')