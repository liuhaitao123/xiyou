# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from service.models import WriteType, Writer, VisaType, Visa
from university.models import Country
from operation.models import UserCart
import json


# Create your views here.


class DocView(View):
    def get(self, request):
        all_types = WriteType.objects.all()
        all_docs = Writer.objects.all()

        type_id = request.GET.get('type', '')
        if type_id:
            all_docs = Writer.objects.filter(type=int(type_id))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_docs, 3, request=request)

        docs = p.page(page)

        return render(request, 'doc.html', {'all_types': all_types,
                                             'all_docs': docs,
                                             'type_id': type_id,
                                             })

    def post(self, request):
        store_id = request.POST.get('doc_id', '')
        store_type = request.POST.get('store_type', '')
        number = request.POST.get('nums', 1)

        json_data = {'status': 'success'}

        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('user:login'))
        try:	
            records = UserCart.objects.get(user=request.user, store_id=store_id, store_type=store_type)
        except:
            records = None
		
        if records:
            records.nums = records.nums + int(number)
            records.save()
            return HttpResponse(json.dumps(json_data), content_type="application/json")
        else:
            user_cart = UserCart()
            user_cart.user = request.user
            user_cart.store_id = store_id
            user_cart.store_type = store_type
            user_cart.nums = int(number)
            user_cart.save()
            return HttpResponse(json.dumps(json_data), content_type="application/json")


class VisaView(View):
    def get(self, request):
        all_country = Country.objects.all()
        all_types = VisaType.objects.all()
        all_visas = Visa.objects.all()

        type_id = request.GET.get('type', '')
        if type_id:
            all_visas = Visa.objects.filter(type=int(type_id))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_visas, 2, request=request)

        visas = p.page(page)

        return render(request, 'visa.html', {'all_types': all_types,
                                             'all_visas': visas,
                                             'type_id': type_id,
                                             'all_country':all_country,
                                             })


class DocDetailView(View):
    def get(self, request, doc_id):
        doc = Writer.objects.get(pk=int(doc_id))
        return render(request, 'doc-detail.html', {'doc': doc})
