# -*- coding:utf-8 -*-
from django import forms
import chardet
from jwc import *
from jwcsite.stu_service.models import psd
import hashlib

class JsForm(forms.Form):
    classroom = forms.CharField(label="教学楼名称")
    sessionstart = forms.CharField(label='开始节次')
    sessionend = forms.CharField(label = '结束节次')

    def clean_classroom(self):
        classroom = self.cleaned_data['classroom']
        if not classroom in [u'正心',u'诚意',u'致知']:
            raise forms.ValidationError("目前只能输入'正心'，'诚意'，'致知'哦")
        return classroom

    def clean_sessionstart(self):
        sessionstart = self.cleaned_data['sessionstart']
        isin=False
        if not sessionstart in ['1','3','5','7','9']:
            raise forms.ValidationError('开始节次仅可以输入奇数呢')
        return sessionstart

    def clean_sessionend(self):
        session=self.cleaned_data
        sessionend = session['sessionend']
        isin=False
        if not sessionend in ['2','4','6','8','10']:
            raise forms.ValidationError('结束节次要输入偶数哦')
        end=(int)(session['sessionend'])
        try:
            start=(int)(session['sessionstart'])
            if end<start:
                raise forms.ValidationError(u'您输入的结束节次是不是比结束节次要小呢')
            return sessionend
        except KeyError:
            return sessionend
            

class FeedbackForm(forms.Form):
    feedbackarea = forms.CharField(widget = forms.Textarea,label = u"反馈内容")

    def clean_feedbackarea(self):
        data = self.cleaned_data['feedbackarea']
        if len(data)<1:
            raise forms.ValidationError(u"不能为空哦!!!")
        return data

class ViewkbForm(forms.Form):
    bh=forms.CharField(max_length=8,label = u"输入班号")

    def clean_bh(self):
        bh = self.cleaned_data['bh']
        kbpage= jwc()
        kbpage.set_kb(bh)
        if not kbpage.view_data():
            raise forms.ValidationError(u"您所查询的班级不存在")
        return bh

class MyownForm(forms.Form):
    password=forms.CharField(label = "密码",widget= forms.PasswordInput())
    seedata = forms.CharField(required = False,label = "查看数据,输入1",max_length=1)
    seefeed = forms.CharField(required = False,label = "查看反馈,输入1",max_length=1)
    printdata = forms.CharField(required = False,label = "测试数据,输入第几周",max_length=2)
    intodata = forms.CharField(required = False,label = "插入数据,输入第几周",max_length=2)

    def clean_password(self):
        password = self.cleaned_data['password'].strip()
        m= hashlib.md5(password)
        password = m.hexdigest()
        db_password = psd.objects.get(user='cloudaice')
        if not password == db_password.password:
            raise forms.ValidationError(u'密码错误')
        return password

    def clean_intodata(self):
        s=['','','','']
        s[0]=self.cleaned_data['seedata']
        s[1]=self.cleaned_data['seefeed']
        s[2]=self.cleaned_data['printdata']
        s[3]=self.cleaned_data['intodata']
        count=0;
        for value in range(4):
            if  s[value]:
                count+=1
        if not count == 1:
            raise forms.ValidationError(u'重新输入')
        return s[3]


                

