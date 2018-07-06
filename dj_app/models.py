# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class JiraPost(models.Model):
    ppid = models.CharField(max_length=10)
    jira_url = models.CharField(max_length=200)
    project = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    summary = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    class Meta:
       ordering = ('-timestamp',)