# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader
import os

# Create your views here.
def index(request):
    #return HttpResponse('Hello, world.')
    return render(request, 'index.html')
def php_publish(request):
    return render(request, 'php_publish.html')
def php_command(request):
    result = os.system(str(request))
    return render_to_response("index.html", {"message": result})