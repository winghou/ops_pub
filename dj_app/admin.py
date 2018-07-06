# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dj_app import models
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(models.BlogPost, BlogPostAdmin)


class JiraPostAdmin(admin.ModelAdmin):
    list_display = ('ppid', 'jira_url', 'timestamp')

admin.site.register(models.JiraPost, JiraPostAdmin)