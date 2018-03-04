# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
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
    os.system("dir")