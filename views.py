# -*- coding: utf-8 -*-
import os
import sys

import xlrd as xlrd
from django.db import transaction
from django.http import HttpResponse, FileResponse

from common.mymako import render_mako_context, render_json
from conf.default import BASE_DIR, PROJECT_PATH, PROJECT_ROOT
from home_application import models
from home_application.commons.commons import get_script, get_businesses
import datetime

reload(sys)
sys.setdefaultencoding('utf8')


def task(request):
    """
    执行任务页面
    """
    get_app = get_businesses(request)
    return render_mako_context(request, '/home_application/task.html')


def up_file(request):
    '''
    上传文件
    :param request:
    :return:
    '''
    print 1111111
    myFile = request.FILES.get("files", None)  # 获取上传的文件，如果没有文件，则默认为None
    if not myFile:
        return HttpResponse("no files for upload!")
    path1 = PROJECT_ROOT + '\upload'
    destination = open(os.path.join(path1, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    return render_json({'filename': myFile.name})


def excel_upload(request):
    '''
    下载excel
    :param request:
    :return:
    '''
    filename = request.GET.get('temp_name', '')
    path2 = PROJECT_ROOT + '/upload/' + filename
    file = open(path2, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response
