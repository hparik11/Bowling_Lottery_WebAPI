from django.db import models
from django.utils import timezone

# Create your models here.

class Bowler(models.Model):

    modified = models.DateTimeField()
    created = models.DateTimeField(editable=False)
    name = models.CharField(max_length=200)
    #email = models.EmailField(max_length=200)
    amount = models.IntegerField(default=1000)



    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
    
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('created',)



class Lottery(models.Model):
    lot_name = models.CharField(max_length=200)
