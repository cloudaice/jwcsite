# -*- coding:utf-8 -*-
from django import forms

class JsForm(forms.Form):
    classroom = forms.CharField()
    sessionstart = forms.CharField()
    sessionend = forms.CharField()
    ''' 
    def clean_classroom(self):
        classroom = self.cleaned_data['classroom']
        isin=False
        for room in ["正心","诚意","致知"]:
            if room in classroom:
                isin=True
        if not isin:
            raise forms.ValidationError('input proper value')
        return classroom

    def clean_sessionstart(self):
        sessionstart = self.cleaned_data['sessionstart']
        isin=Flase
        for start in ['1','3','5','7','9']:
            if start == sessionstart:
                isin = True
        if not isin:
            raise forms.ValidationError('the digital is not right')
        return sessionstart

    def clean_sessionend(self):
        sessionend = self.cleaned_data['sessionend']
        isin=Flase
        for start in ['2','4','6','8','10']:
            if start == sessionend:
                isin = True
        if not isin:
            raise forms.ValidationError('the digital is not right')
        return sessionend
     '''

