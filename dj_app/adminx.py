# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.contrib import admin
import xadmin
# from dj_app import models
from xadmin import views
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    site_title = "zsmlinux ops system"
    site_footer = "http://www.zsmlinux.org"
    #menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSetting)