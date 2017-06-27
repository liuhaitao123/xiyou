# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse

from university.models import Country, Level, University, MajorField, Major, Scenery


# Create your views here.


class UniversityView(View):
    def get(self, request):
        all_country = Country.objects.all()
        all_level = Level.objects.all()
        all_university = University.objects.all()

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
                                                   })


class EstimateView(View):
    def get(self, request):
        return render(request, 'estimate.html')


class StrategyView(View):
    def get(self, request):
        return render(request, 'strategy.html')