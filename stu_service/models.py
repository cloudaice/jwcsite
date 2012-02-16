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
        ordering = ['room']

class feedback_data(models.Model):
    terminal = models.CharField(max_length = 50)
    date = models.CharField(max_length=30)
    feedback_data = models.TextField()

    def __unicode__(self):
        return self.terminal

    class Meta:
        ordering = ['date']
