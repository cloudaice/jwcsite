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
