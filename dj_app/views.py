# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from dj_app.models import BlogPost
from datetime import datetime
import os

# Create your views here.
def index(request):
    #return HttpResponse('Hello, world.')
    return render(request, 'index.html')
def php_publish(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("php_publish.html")
    c = Context().update({'posts': posts})
    return HttpResponse(t.render(c))