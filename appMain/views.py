from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse

from appMain.models import Student as S
# Create your views here.

def home(request):

    assert isinstance(request, HttpRequest)

    context = RequestContext(
        request,
        {
            'title': 'Walk on Prize Day',
        }
    )

    homeRenderer = render(
        request,
        'appMain/index.html',
        context_instance=context
    )

    return homeRenderer

def list(request):

    assert isinstance(request, HttpRequest)

    form = int(request.GET['form'])

    boys = S.objects.filter(Gender=1,Form=form).order_by('LName')
    girls = S.objects.filter(Gender=2,Form=form).order_by('LName')

    numPairs = min([len(boys),len(girls)])
    if len(boys) > len(girls):
        greater = boys
        lesser = girls
    else:
        greater = girls
        lesser = boys
        
    extra = [None for i in range(numPairs)]
    surplus = len(greater) - numPairs

    extra[numPairs-surplus:] = greater[numPairs:]

    zipped = zip(greater,lesser,extra)

    context = RequestContext(
        request,
        {
            'title': 'Walk on Prize Day',
            'zipped' : zipped
        }
    )

    listRenderer = render(
        request,
        'appMain/list.html',
        context_instance=context
    )

    return listRenderer
