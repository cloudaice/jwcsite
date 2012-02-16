#@+leo-ver=5-thin
#@+node:cloudaice.20120216102454.1132: * @file /home/cloudaice/pyrepo/jwcsite/stu_service/forms.py
#@@language python
#@@tabwidth -4
#@+others
#@+node:cloudaice.20120216102454.1133: ** forms declarations
# -*- coding:utf-8 -*-
from django import forms
import chardet

#@+node:cloudaice.20120216102454.1134: ** class JsForm
class JsForm(forms.Form):
    classroom = forms.CharField(label="教学楼名称")
    sessionstart = forms.CharField(label='开始节次')
    sessionend = forms.CharField(label = '结束节次')

    #@+others
    #@+node:cloudaice.20120216102454.1135: *3* clean_classroom
    def clean_classroom(self):
        classroom = self.cleaned_data['classroom']
        if not classroom in [u'正心',u'诚意',u'致知']:
            raise forms.ValidationError("只能输入'正心'，'诚意'，'致知'")
        return classroom

    #@+node:cloudaice.20120216102454.1136: *3* clean_sessionstart
    def clean_sessionstart(self):
        sessionstart = self.cleaned_data['sessionstart']
        isin=False
        if not sessionstart in ['1','3','5','7','9']:
            raise forms.ValidationError('请输入奇数节次')
        return sessionstart

    #@+node:cloudaice.20120216102454.1137: *3* clean_sessionend
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

    #@-others
#@-others
#@-leo
