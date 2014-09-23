# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from ocupa.models import Questao


def index(request):
    return render(request, 'ocupa/index.html')

def questions(request):
    questions = Questao.objects.all()
    data = serializers.serialize("json", questions)
    return HttpResponse(data, content_type='application/json')
