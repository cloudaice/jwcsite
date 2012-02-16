# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from jwcsite.stu_service.models import js_status
from jwcsite.stu_service.forms import JsForm,feedbackarea
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
        form = feedbackarea(request.POST)


