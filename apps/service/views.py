# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from .models import WriteType, Writer, Visa

# Create your views here.


class DocView(View):
    def get(self, request):
        all_types = WriteType.objects.all()
        all_docs = Writer.objects.all()
		
        type_id = request.GET.get('type')
        if type_id:
            all_docs = Writer.objects.filter(type=int(type_id))
        return render(request, 'doc.html', {'all_types':all_types, 'all_docs':all_docs})


class VisaView(View):
    def get(self, request):
        return render(request, 'visa.html')
