# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from jwcsite.stu_service.models import js_status,feedback_data,psd,class_table
from jwcsite.stu_service.forms import JsForm,FeedbackForm,ViewkbForm,MyownForm
import time
from jwc import *
from jwcsite.stu_service import w_data
from datetime import datetime
BEGIN_WEEK=35

def home_page(request):
    if request.method == 'POST':
        form = JsForm(request.POST)
        if form.is_valid():
            js =form.cleaned_data 
            room_tables=[]
            now_weeks = datetime.now().strftime('%W')
            school_week = int(now_weeks)-BEGIN_WEEK 
            str_school_week=str(school_week)
            if len(str_school_week)==1:
                str_school_week = '0'+str_school_week;
            rooms=js_status.objects.filter(room__contains=js['classroom'],weeks=str_school_week,term='2012-2')
            start=int(js['sessionstart'])
            end = int(js['sessionend'])
            times= (end-start+1)/2
            weekday = int(time.strftime('%w',time.localtime(time.time())))
            s = (weekday-1)*5+(start-1)/2
            for room in rooms:
                isin=True
                for c in range(times):
                    if not room.status[s+c]=='0':
                        isin = False
                        break
                if isin:
                    room_tables.append(room.room)
            new_room_tables=[]
            if  (len(room_tables) % 3) :
                for key in range(3-(len(room_tables) % 3)):
                    room_tables.append('')
            for key in range(len(room_tables)):
                if key % 3==0:
                    new_room_tables.append((room_tables[key],room_tables[key+1],room_tables[key+2]))
            return render_to_response('home_page.html',{'form':form,'room_tables':new_room_tables,"inquiry":'yes'})
            #return HttpResponse('%s %s' %(s,times))
    else:
        form = JsForm()
    return render_to_response('home_page.html',{'form':form})

def feedback(request):
    if request.method == 'POST':
        agent=request.META.get('HTTP_USER_AGENT','unknow')
        #datetime = time.ctime()
        form =  FeedbackForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data['feedbackarea']
            feedback_data(
                    terminal=agent,
                    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    feedbackdata=data,
                    ).save()
            return render_to_response("feedback.html",{'feedback_ok':'yes'})
    else:
        form = FeedbackForm()
    return render_to_response("feedback.html",{'form':form})
'''
def seefeed(request):
        feedbacks= feedback_data.objects.all()
        html=[]
        for i in feedbacks:
            html.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(i.terminal,i.date,i.feedbackdata))
        return HttpResponse(u"<table border='3'>%s</table>"% '\n'.join(html))
def seedata(request):
    datas = js_status.objects.all()
    html=[]
    dataindex=["room","status","weeks","term","area"]
    for i in datas:
        temp="<tr>"
        temp+=("<td>%s</td>" %i.room)
        temp+=("<td>%s</td>" %i.status)
        temp+=("<td>%s</td>" %i.weeks)
        temp+=("<td>%s</td>" %i.term)
        temp+=("<td>%s</td>" %i.area)
        temp+="</tr>"
        html.append(temp)
    return HttpResponse(u"<table border='3'>%s</table>"% '\n'.join(html))
'''
def viewkb(request):
    if request.method=='POST':
        form = ViewkbForm(request.POST)
        if form.is_valid():
            bh = form.cleaned_data['bh']
            try:
                tables=class_table.objects.get(classnumber=bh)
            except class_table.DoesNotExist:
                kbpage = jwc()
                kbpage.set_kb(bh)
                html = kbpage.view_data()
                class_table(
                        classnumber=bh,
                        classtable=html
                        ).save()
                return HttpResponse(html)
            else:
                return HttpResponse(tables.classtable)
    else:
        form = ViewkbForm()
    return render_to_response('kbpage.html',{'form':form})
    
def myown(request):
    if request.method == 'POST':
        form = MyownForm(request.POST)
        if form.is_valid():
            s=['','','','']
            s[0]=form.cleaned_data['seedata']
            s[1]=form.cleaned_data['seefeed']
            s[2]=form.cleaned_data['printdata']
            s[3]=form.cleaned_data['intodata']
            value=0
            for key in range(4):
                if s[key]:
                    value = key
                    break
            if value ==0:
                dataform= []
                datas = js_status.objects.all()
                for data in datas:
                    temp = (data.room,data.status,data.weeks,data.term,data.area)
                    dataform.append(temp)
                return render_to_response('myown.html',{'dataform':dataform})
            elif value ==1:
                feedform=[]
                feeds = feedback_data.objects.all()
                for feed in feeds:
                    temp = (feed.terminal,feed.date,feed.feedbackdata)
                    feedform.append(temp)
                return render_to_response('myown.html',{'feedform':feedform})
            elif value ==2:
                oneform = []
                week = s[value].strip()
                newpage = jwc()
                newpage.set_js(week,'一校区')
                js_data = jsparser()
                js_data.feed(newpage.view_data())
                r = js_data.get_room()
                s = js_data.get_status()
                if len(r)== len(s):
                    for key in range(len(r)):
                        temp = (r[key],s[key],week,'2012-2','一校区')
                        oneform.append(temp)
                    return render_to_response('myown.html',{'dataform':oneform})
                return HttpResponse("some thing wrong")
            else:
                return w_data.insertdata(s[value])
    else:
        form = MyownForm()
    return render_to_response('myown.html',{'form':form})

