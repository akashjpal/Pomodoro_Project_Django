from django.db import models

class Timers(models.Model):
  title = models.CharField(max_length=100)
  hours = models.IntegerField(default=0)
  minutes = models.IntegerField(default=25)
  seconds = models.IntegerField(default=0)
  uuid = models.IntegerField(default=0)
  
