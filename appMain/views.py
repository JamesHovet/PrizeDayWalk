from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse

from appMain.models import Student
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

    context = RequestContext(
        request,
        {
            'title': 'Walk on Prize Day'
        }
    )

    listRenderer = render(
        request,
        'appMain/list.html',
        context_instance=context
    )

    return listRenderer
