# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'home_application.task.views',
    (r'^$', 'task'),
    (r'^create_task/$', 'create_task'),
    (r'^up_file/$', 'up_file'),
    url(r'^excel_upload/', views.excel_upload, name='uploads'),
)
