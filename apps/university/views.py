# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse

from university.models import Country, Level, University
from information.models import Article, WinCase
from users.models import BannerOther
from operation.models import UserAsk


# Create your views here.


class UniversityView(View):
    def get(self, request):
        all_country = Country.objects.all()
        all_level = Level.objects.all()
        all_university = University.objects.all()
        banner_list = BannerOther.objects.all()[:3]

        country_id = request.GET.get('country', '')
        type = request.GET.get('type', '')
        level_id = request.GET.get('level', '')

        if country_id:
            all_university = all_university.filter(country=int(country_id))

        if type:
            all_university = all_university.filter(type=type)

        if level_id:
            all_university = all_university.filter(level=int(level_id))

        return render(request, 'university.html', {'all_country': all_country,
                                                   'all_level': all_level,
                                                   'all_university': all_university,
                                                   'country_id': country_id,
                                                   'type': type,
                                                   'level_id': level_id,
                                                   'banner_list': banner_list
                                                   })


class UniversityDetailView(View):
    def get(self, request, university_id):
        university = University.objects.get(pk=int(university_id))
        return render(request, 'university-detail.html', {'university': university})


class EstimateView(View):
    def get(self, request):
        return render(request, 'estimate.html')


class StrategyView(View):
    def get(self, request):
        all_country = Country.objects.all()
        country_id = request.GET.get('country', '1')
        all_article = Article.objects.all().filter(status=1)
        win_case = WinCase.objects.all()[:6]
        ask_list =  UserAsk.objects.all()[:3]

        if country_id:
            all_article = all_article.filter(country=int(country_id))	
            art_strategy = 	all_article.filter(category='gl')[:5]
            art_forum = 	all_article.filter(category='lt')[:5]
            art_counsel = 	all_article.filter(category='zx')[:5]			

        return render(request, 'strategy.html', {'all_country': all_country, 'art_strategy': art_strategy, 'art_forum': art_forum, 'art_counsel': art_counsel, 'country_id': country_id, 'win_case': win_case, 'ask_list': ask_list})


class StrategyListView(View):
    def get(self, request):
        type = request.GET.get('type', 'gl')
        all_article = Article.objects.all()

        if type and type != 'al':
            all_article = all_article.filter(category=type)
			
        if type == 'al':
            all_article = WinCase.objects.all()

        return render(request, 'strategy-list.html', {'all_article': all_article, 'type': type})


class ArticleView(View):
    def get(self, request, article_id):
        article = Article.objects.get(pk=int(article_id))
        return render(request, 'article.html', {'article': article})
