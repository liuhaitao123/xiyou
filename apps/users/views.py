# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
import json

from forms import RegisterForm, LoginForm
from operation.models import HighApply, UserAsk, UserMajor
from users.models import BannerIndex
from information.models import WinCase, Article
from university.models import University

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
                return HttpResponseRedirect(reverse('user:index'))
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
        univer_ame = University.objects.filter(show_index=1).filter(country=1)[:8]
        univer_eng = University.objects.filter(show_index=1).filter(country=2)[:8]
        univer_can = University.objects.filter(show_index=1).filter(country=3)[:8]
        univer_aus = University.objects.filter(show_index=1).filter(country=4)[:8]
        ask_list = UserAsk.objects.all()[:3]
        infor_zx = Article.objects.filter(category='zx')[:6]
        infor_gl = Article.objects.filter(category='gl')[:6]

        return render(request, 'index.html', {'banner_list': banner_list,
                                              'win_case_one': win_case_one,
                                              'win_case_two': win_case_two,
                                              'univer_ame': univer_ame,
                                              'univer_eng': univer_eng,
                                              'univer_can': univer_can,
                                              'univer_aus': univer_aus,
                                              'ask_list': ask_list,
                                              'infor_zx': infor_zx,
                                              'infor_gl': infor_gl,
                                              })


class HighApplyView(View):
    def get(self, request):
        return render(request, 'highapply.html')

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('user:login'))
        else:
            user_id = request.user.id
            real_name = request.POST.get('real_name', '')
            country = request.POST.get('country', '')
            type = request.POST.get('type', '')
            major = request.POST.get('major', '')
            high_apply = HighApply()
            high_apply.user_id = user_id
            high_apply.real_name = real_name
            high_apply.type = type
            high_apply.country = country
            high_apply.major = major
            high_apply.save()
            json_data = {'status': 'success'}
            return HttpResponse(json.dumps(json_data), content_type="application/json")


class UsercenterView(View):
    def get(self, request):
        return render(request, 'usercenter.html')


class MyApplyView(View):
    def get(self, request):
        apply_list = UserMajor.objects.filter(user=request.user)
        return render(request, 'usercenter-myapply.html', {'apply_list': apply_list})


class MyOrderView(View):
    def get(self, request):
        return render(request, 'usercenter-myorder.html')


class MyAskView(View):
    def get(self, request):
        question_list = UserAsk.objects.filter(user=request.user)
        return render(request, 'usercenter-myask.html', {'question_list': question_list})


class MyQstView(View):
    def get(self, request):
        return render(request, 'usercenter-myquestion.html')

    def post(self, request):
        ask = UserAsk()
        ask.user = request.user
        ask.problem = request.POST.get('problem', '')
        ask.save()

        return HttpResponseRedirect(reverse('user:myask'))


class CaseView(View):
    def get(self, request, case_id):
        wincase = WinCase.objects.get(id=int(case_id))
        return render(request, 'wincase.html', {'wincase': wincase})

