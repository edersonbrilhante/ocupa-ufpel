# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from ocupa.models import Questao
from ocupa.forms import QuestaoForm


def index(request):
    return render(request, 'ocupa/index.html')

def questions(request):
    questions = Questao.objects.all()
    data = serializers.serialize("json", questions)
    return HttpResponse(data, content_type='application/json')

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = QuestaoForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Questao(docfile=request.FILES['imagem'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('ocupa.views.list'))
    else:
        form = QuestaoForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Questao.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'ocupa/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
