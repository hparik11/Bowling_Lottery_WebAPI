from django.db import models
#from django.utils import timezone
import datetime


# Create your models here.

class Bowler(models.Model):

    modified = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(default=datetime.datetime.now,editable=False)
    name = models.CharField(max_length=200)
    
    amount = models.IntegerField(default=1000)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('created',)


class League(models.Model):

    name = models.CharField(max_length=200)
    bowler_id = models.IntegerField(default=0)

    
    def __unicode__(self):
        return self.name

class Lottery(models.Model):

    name = models.CharField(max_length=200)
    bowler_id = models.IntegerField(default=0)

    
    def __unicode__(self):
        return self.name
