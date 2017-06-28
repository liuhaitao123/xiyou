# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View

from service.models import WriteType, Writer, VisaType, Visa
from university.models import Country


# Create your views here.


class DocView(View):
    def get(self, request):
        all_types = WriteType.objects.all()
        all_docs = Writer.objects.all()
		
        type_id = request.GET.get('type')
        if type_id:
            all_docs = Writer.objects.filter(type=int(type_id))
        return render(request, 'doc.html', {'all_types': all_types,
                                             'all_docs': all_docs,
                                             'type_id': type_id,
                                             })


class VisaView(View):
    def get(self, request):
        all_country = Country.objects.all()
        all_types = VisaType.objects.all()
        all_visas = Visa.objects.all()

        type_id = request.GET.get('type')
        if type_id:
            all_visas = Visa.objects.filter(type=int(type_id))
        return render(request, 'visa.html', {'all_types': all_types,
                                             'all_visas': all_visas,
                                             'type_id': type_id,
											 'all_country':all_country,
                                             })
