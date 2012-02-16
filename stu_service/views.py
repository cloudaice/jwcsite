# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from jwcsite.stu_service.models import js_status,feedback_data
from jwcsite.stu_service.forms import JsForm,FeedbackForm
import time

def home_page(request):
    if request.method == 'POST':
        form = JsForm(request.POST)
        if form.is_valid():
            js=form.cleaned_data 
            room_tables=[]
            rooms=js_status.objects.filter(room__icontains=js['classroom'])
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
                    room_tables.append(None)
            for key in range(len(room_tables)):
                if key % 3==0:
                    new_room_tables.append((room_tables[key],room_tables[key+1],room_tables[key+2]))
            return render_to_response('home_page.html',{'form':form,'room_tables':new_room_tables})
            #return HttpResponse('%s %s' %(s,times))
    else:
        form = JsForm()
    return render_to_response('home_page.html',{'form':form})

def feedback(request):
    if request.method == 'POST':
        agent=request.META.get('HTTP_USER_AGENT','unknow')
        datetime = time.ctime()
        form =  FeedbackForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data['feedbackarea']
            feedback_data(
                    terminal=agent,
                    date = datetime,
                    feedbackdata=data,
                    ).save()
            return HttpResponse(u"<p>谢谢您的反馈</p>")
    else:
        form = FeedbackForm()
    return render_to_response("feedback.html",{'form':form})

def seefeed(request):
        feedbacks=feedback_data.objects.all()
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













