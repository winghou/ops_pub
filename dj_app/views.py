# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from dj_app.models import BlogPost,JiraPost
from datetime import datetime
import os
from django import forms
from models import User
from django.contrib import auth
import pdb

# Create your views here.
def index(request):
    #return HttpResponse('Hello, world.')
    return render(request, 'index.html')
def php_publish(request):
    posts = JiraPost.objects.all()[:1]
    #t = loader.get_template("php_publish.html")
    #c = Context().update({'posts': posts})
    #return HttpResponse(t.render(c))
    #return render_to_response('php_publish.html', {'posts':posts,})
    #                        RequestContext(request))
    return  render(request, 'php_publish.html', {'posts':posts,})

def net_publish(request):
    posts = BlogPost.objects.all()[:1]
    #t = loader.get_template("php_publish.html")
    #c = Context().update({'posts': posts})
    #return HttpResponse(t.render(c))
    #return render_to_response('php_publish.html', {'posts':posts,})
    #                        RequestContext(request))
    return  render(request, 'net_publish.html', {'posts':posts,})

def create_blogpost(request):
    if request.method == "POST":
        BlogPost(
            title = request.POST.get('title'),
            body = request.POST.get('body'),
            timestamp = datetime.now(),
        ).save()
    return HttpResponseRedirect('net_publish.html')

def get_jira_info(request):
    ppid = request.POST.get('PPID')
    url = "http://jira.yaochufa.com:8080/browse/PP-%s" % ppid
    if request.method == "POST":
        JiraPost(
            ppid = request.POST.get('PPID'),
            jira_url = url,
            timestamp = datetime.now(),
        ).save()
    return HttpResponseRedirect('php_publish.html')

def login(request):
    if request.method == "POST":
        uf = UserFormLogin(request.POST)
        if uf.is_valid():

            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = User.objects.filter(username=username, password=password)
            if (len(userResult)>0):
                return render_to_response('/djapp/index.html',{'operation':"登陆"})
            else:
                return HttpResponse("用户不存在")
    else:
        uf = UserFormLogin()

    return render_to_response('login.html',{'uf':uf})

class UserFormLogin(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())