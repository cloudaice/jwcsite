#-*- coding: utf-8 -*-
'''
call this file can input the data into database
'''
from jwc import *
from jwcsite.stu_service.models import js_status
from django.http import HttpResponse

def insertdata(request):
    newpage = jwc()
    newpage.set_js('01','一校区')
    js_data = jsparser()
    js_data.feed(newpage.view_data())
    r = js_data.get_room()
    s = js_data.get_status()
    if len(r)==len(s):
        js_status.objects.all().delete()
        for key in range(len(r)):
            js_status(
                    room=r[key],
                    status=s[key],
                    weeks='01',
                    term='2012-1',
                    area='一校区',
                    ).save()
    return  HttpResponse('data has insert')

