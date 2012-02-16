#@+leo-ver=5-thin
#@+node:cloudaice.20120216102454.1158: * @file /home/cloudaice/pyrepo/jwcsite/stu_service/models.py
#@@language python
#@@tabwidth -4
#@+others
#@+node:cloudaice.20120216102454.1159: ** models declarations
from django.db import models

#@+node:cloudaice.20120216102454.1160: ** class js_status
class js_status(models.Model):
    room = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    weeks = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    area = models.CharField(max_length=20)

    #@+others
    #@+node:cloudaice.20120216102454.1161: *3* __unicode__
    def __unicode__(self):
        return self.room

    #@+node:cloudaice.20120216102454.1162: *3* class Meta
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
    #@-others
#@-others
#@-leo
