from django.db import models

class PomodoroSession(models.Model):
    is_running = models.BooleanField(default=False)
    duration = models.IntegerField(default=25)
    time_elapsed = models.IntegerField(default=0)
