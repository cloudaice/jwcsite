# -*- coding:utf-8 -*-
from django.db import models

class js_status(models.Model):
    room = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    weeks = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    area = models.CharField(max_length=20)

    def __unicode__(self):
        return self.room

    class Meta:
        ordering = ['weeks']

class feedback_data(models.Model):
    terminal = models.CharField(max_length = 50)
    date = models.CharField(max_length=30)
    feedbackdata = models.TextField()

    def __unicode__(self):
        return u"%s\n %s" %(self.date,self.feedbackdata)

    class Meta:
        ordering = ['-date']

class psd(models.Model):
    user = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    
