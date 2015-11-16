from django.db import models

# Create your models here.

class Bowler(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    created = models.DateTimeField('date published')
    password = models.CharField(max_length=6)
    amount = models.IntegerField(default=1000)


    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('created',)
