from email.policy import default
from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Usage(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    is_on = models.BooleanField()
    def __str__(self):
        return f"{self.date} - {'On' if self.is_on else 'Off' }"

class AggUsage(models.Model):
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    class Meta:
        

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.start_time = timezone.now()

    def __str__(self):
        return f"{self.start_time} til {self.end_time}"
    
class ScheduledEvent(models.Model):

    start_time = models.DateTimeField(auto_now_add=False, default=timezone.now)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    NONE = "None"
    repeat_choices = ((DAILY, "Daily"), (WEEKLY, "Weekly"), (NONE, "None"))
    repeat = models.CharField(max_length=6, choices = repeat_choices, default=NONE)

    ON = "ON"
    OFF = "OFF"
    TOG = "TOG"
    TOGGLE_CHOICES = ((ON, "On"), (OFF, "Off"), (TOG, "Toggle"))
    command = models.CharField(max_length=6, choices=TOGGLE_CHOICES, default=TOG)

    def __str__(self):
        return f"{self.command} - {self.start_time}"

    def del_sched(self):
        '''
        Deletes a scheduled event from being acted upon but not from the db.

        sets deleted to true and reschedules the new one if repeat is not none.
        '''
        self.deleted = True
        self.save()
        print(self.repeat)
        if self.repeat == "DAILY" or self.repeat == "WEEKLY":
            
            self.pk = None
            self.deleted = False
            self.completed = False
            if self.repeat == "DAILY":
                self.start_time += timedelta(days=1)
            else: 
                self.start_time += timedelta(weeks=1)
            self.save()
