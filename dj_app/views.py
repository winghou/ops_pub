# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from dj_app.models import BlogPost
from datetime import datetime
import os

# Create your views here.
def index(request):
    #return HttpResponse('Hello, world.')
    return render(request, 'index.html')
def php_publish(request):
    posts = BlogPost.objects.all()[:1]
    #t = loader.get_template("php_publish.html")
    #c = Context().update({'posts': posts})
    #return HttpResponse(t.render(c))
    #return render_to_response('php_publish.html', {'posts':posts,})
    #                        RequestContext(request))
    return  render(request, 'php_publish.html', {'posts':posts,})

def create_blogpost(request):
    if request.method == "POST":
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now(),
        ).save()
    return HttpResponseRedirect('php_publish.html')