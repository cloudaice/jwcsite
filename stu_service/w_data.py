#@+leo-ver=5-thin
#@+node:cloudaice.20120216102454.1170: * @file /home/cloudaice/pyrepo/jwcsite/stu_service/w_data.py
#@@language python
#@@tabwidth -4
#@+others
#@+node:cloudaice.20120216102454.1171: ** w_data declarations
#-*- coding: utf-8 -*-
'''
call this file can input the data into database
'''
from jwc import *
from jwcsite.stu_service.models import js_status
from django.http import HttpResponse

#@+node:cloudaice.20120216102454.1172: ** insertdata
def insertdata(request):
    newpage = jwc()
    newpage.set_js('21','一校区')
    js_data = jsparser()
    js_data.feed(newpage.view_data())
    r = js_data.get_room()
    s = js_data.get_status()
    if len(r)==len(s):
        for key in range(len(r)):
            js_status(
                    room=r[key],
                    status=s[key],
                    weeks='21',
                    term='2011-2',
                    area='一校区',
                    ).save()
    return  HttpResponse('data has insert')

#@-others
#@-leo
