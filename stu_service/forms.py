# -*- coding:utf-8 -*-
from django import forms
import chardet
from jwc import *

class JsForm(forms.Form):
    classroom = forms.CharField(label="教学楼名称")
    sessionstart = forms.CharField(label='开始节次')
    sessionend = forms.CharField(label = '结束节次')

    def clean_classroom(self):
        classroom = self.cleaned_data['classroom']
        if not classroom in [u'正心',u'诚意',u'致知']:
            raise forms.ValidationError("只能输入'正心'，'诚意'，'致知'")
        return classroom

    def clean_sessionstart(self):
        sessionstart = self.cleaned_data['sessionstart']
        isin=False
        if not sessionstart in ['1','3','5','7','9']:
            raise forms.ValidationError('请输入奇数节次')
        return sessionstart

    def clean_sessionend(self):
        session=self.cleaned_data
        sessionend = session['sessionend']
        isin=False
        if not sessionend in ['2','4','6','8','10']:
            raise forms.ValidationError('请输入偶数节次')
        end=(int)(session['sessionend'])
        start=(int)(session['sessionstart'])
        if end<start:
            raise forms.ValidationError(u'结束节次不能比开始节次小')
        return sessionend

class FeedbackForm(forms.Form):
    feedbackarea = forms.CharField(widget = forms.Textarea,label = u"反馈内容")

    def clean_feedbackarea(self):
        data = self.cleaned_data['feedbackarea']
        if len(data)<5:
            raise forms.ValidationError(u"字数必须大于5")
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

